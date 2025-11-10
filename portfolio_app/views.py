"""Views for portfolio_app app"""

from django.core.cache import cache
from django.views.generic import DetailView, ListView
from django.db.models import Q, F
from django_visit_count.utils import is_new_visit
from portfolio_app.models import Portfolio, Project, ResumeJobs, ResumeSkills, ResumeEducation, ResumeCertifications
from portfolio_app.wordcloud import show_wordcloud
from portfolio_app.utils import get_project_dependencies


class HomeView(ListView):
    """View to display list of projects."""

    model = Project
    context_object_name = "projects"
    template_name = "portfolio_app/index.html"
    paginate_by = 5
    cache_key = "word_cloud_image"

    def get_context_data(self, **kwargs):
        """Get context data for wordcloud image of skills and cache image for reuse."""
        context = super().get_context_data(**kwargs)
        cached_image = cache.get(self.cache_key)
        if cached_image:
            context["wordcloud"] = cached_image

        else:
            wordcloud_image = show_wordcloud(
                list(ResumeSkills.objects.all().values_list("name", flat=True))  # pylint: disable=no-member
            )
            cache.set(self.cache_key, wordcloud_image, timeout=3600)
            context["wordcloud"] = wordcloud_image

        context["portfolio"] = Portfolio.objects.first()  # pylint: disable=no-member
        context["dependencies"] = get_project_dependencies()

        return context

    def get_queryset(self):
        """Get the queryset for the projects list view."""
        queryset = super().get_queryset()

        filter_field_value = self.request.GET.get("filter_field", None)
        filter_field_remove_value = self.request.GET.get("filter_field_remove", None)

        if filter_field_value and not filter_field_remove_value:
            queryset = queryset.filter(tags__name__icontains=filter_field_value)

        return queryset.filter(status="published")  # pylint: disable=no-member

    def get_template_names(self):
        """Get template names based on request type."""
        if self.request.htmx:
            return ["portfolio_app/project-list-elements.html"]

        return self.template_name


# pylint: disable=no-member
class ResumeView(ListView):
    """View to display resume page."""

    model = ResumeJobs
    context_object_name = "jobs"
    template_name = "portfolio_app/resume.html"

    def get_context_data(self, **kwargs):
        """Get context data for the resume view and add related."""
        context = super().get_context_data(**kwargs)

        context["skills"] = ResumeSkills.objects.all()
        context["educations"] = ResumeEducation.objects.all()
        context["certifications"] = ResumeCertifications.objects.all()

        context["portfolio"] = Portfolio.objects.first()

        return context


class ProjectsView(ListView):
    """View to display list of projects."""

    model = Project
    context_object_name = "projects"
    template_name = "portfolio_app/project-all.html"
    paginate_by = 5

    def get_queryset(self):
        """Get the queryset for the projects list view."""
        queryset = super().get_queryset()

        filter_field_value = self.request.GET.get("filter_field", None)
        filter_field_remove_value = self.request.GET.get("filter_field_remove", None)
        search_query = self.request.GET.get("search_field", None)

        if filter_field_value and not filter_field_remove_value:
            queryset = queryset.filter(tags__name__icontains=filter_field_value)

        if search_query:
            queryset = (
                queryset.filter(title__icontains=search_query)
                | queryset.filter(subtitle__icontains=search_query)
                | queryset.filter(content__icontains=search_query)
                | queryset.filter(tags__name__icontains=search_query)
            ).distinct()

        return queryset.filter(status="published")  # pylint: disable=no-member

    def get_template_names(self):
        """Get template names based on request type."""
        if self.request.htmx:
            return "portfolio_app/project-all-partial.html"

        return self.template_name


class ProjectView(DetailView):
    """View to display a single project."""

    model = Project
    context_object_name = "project"
    template_name = "portfolio_app/project-single.html"

    def get_context_data(self, **kwargs):
        """Get context data for the project detail view and add related."""
        context = super().get_context_data(**kwargs)

        if not self.object.project_img:
            context["project_img"] = "default-project.png"

        context["related"] = Project.objects.filter(  # pylint: disable=no-member
            status="published",
        ).filter(
            ~Q(id=self.object.id)
        )[:5]

        return context


class AboutView(DetailView):
    """View to display the about page."""

    model = Portfolio
    context_object_name = "portfolio"
    template_name = "portfolio_app/about.html"

    def get_object(self):  # pylint: disable=arguments-differ
        """Get the single Portfolio instance."""
        portfolio = Portfolio.objects.first()

        if is_new_visit(self.request, portfolio):
            portfolio.total_visits = F("total_visits") + 1
            portfolio.save(update_fields=["total_visits"])
            portfolio.refresh_from_db()

        return portfolio
