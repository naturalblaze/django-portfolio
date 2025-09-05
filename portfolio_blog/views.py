"""Views for portfolio_blog app"""

from django.views.generic import DetailView, ListView
from .models import Post


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


class PostView(DetailView):
    """View to display a single post."""

    model = Post
    context_object_name = "post"
    template_name = "portfolio_blog/post-single.html"

    def get_context_data(self, **kwargs):
        """Get context data for the post detail view and add related."""
        context = super().get_context_data(**kwargs)
        context["related"] = Post.objects.filter(  # pylint: disable=no-member
            status="published", author=self.object.author
        )[:5]

        return context
