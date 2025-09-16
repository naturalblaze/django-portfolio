"""Views for portfolio_blog app"""

from django.views.generic import DetailView, ListView
from django.db.models import Q
from .models import Post, PortfolioJobs, PortfolioSkills, PortfolioEducation, PortfolioCertifications


class HomeView(ListView):
    """View to display list of posts."""

    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(status="published")  # pylint: disable=no-member
    paginate_by = 10

    def get_template_names(self):
        """Get template names based on request type."""
        if self.request.htmx:
            return "portfolio_blog/post-list-elements.html"

        return "portfolio_blog/index.html"


# pylint: disable=no-member
class PortfolioView(ListView):
    """View to display portfolio page."""

    model = PortfolioJobs
    context_object_name = "jobs"
    template_name = "portfolio_blog/portfolio.html"

    def get_context_data(self, **kwargs):
        """Get context data for the portfolio view and add related."""
        context = super().get_context_data(**kwargs)

        context["skills"] = PortfolioSkills.objects.all()
        context["educations"] = PortfolioEducation.objects.all()
        context["certifications"] = PortfolioCertifications.objects.all()

        return context


class PostsView(ListView):
    """View to display list of posts."""

    model = Post
    context_object_name = "posts"
    template_name = "portfolio_blog/posts-all.html"

    def get_queryset(self):
        """Get the queryset for the posts list view."""
        queryset = super().get_queryset()

        filter_field_value = self.request.GET.get("filter_field", None)
        search_query = self.request.GET.get("search_field", None)

        if filter_field_value:
            queryset = queryset.filter(tags__name=filter_field_value)

        if search_query:
            queryset = (
                queryset.filter(title__icontains=search_query)
                | queryset.filter(subtitle__icontains=search_query)
                | queryset.filter(content__icontains=search_query)
                | queryset.filter(tags__name__icontains=search_query)
            ).distinct()

        return queryset.filter(status="published")  # pylint: disable=no-member


class PostView(DetailView):
    """View to display a single post."""

    model = Post
    context_object_name = "post"
    template_name = "portfolio_blog/post-single.html"

    def get_context_data(self, **kwargs):
        """Get context data for the post detail view and add related."""
        context = super().get_context_data(**kwargs)

        if not self.object.post_img:
            context["post_img"] = "default-post.png"

        context["related"] = Post.objects.filter(  # pylint: disable=no-member
            status="published",
        ).filter(
            ~Q(id=self.object.id)
        )[:5]

        return context
