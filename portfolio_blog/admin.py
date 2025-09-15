"""Admin configuration for portfolio_blog app."""

from typing import List
from django.contrib import admin
from .models import Post, Project, PortfolioSkills, PortfolioEducation, PortfolioJobs, PortfolioCertifications


class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post model, to show additional fields in admin panel."""

    list_display = ("title", "subtitle", "slug", "author", "status", "tag_list", "created_at", "updated_at")

    def get_queryset(self, request):
        """Get the queryset for the admin list view, prefetching tags to optimize performance.

        Args:
            request (request): The request object.

        Returns:
            queryset: The queryset with prefetched tags.
        """
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj) -> List[str]:
        """Tag list for a post, displayed in the admin panel.

        Args:
            obj (Any): The Post object.

        Returns:
            List(str): A list of tags associated with the post.
        """
        return ", ".join(o.name for o in obj.tags.all())


class PortfolioSkillsAdmin(admin.ModelAdmin):
    """Admin configuration for PortfolioSkills model."""

    list_display = ("name", "proficiency", "tag_list", "created_at", "updated_at")

    def get_queryset(self, request):
        """Get the queryset for the admin list view, prefetching tags to optimize performance.

        Args:
            request (request): The request object.

        Returns:
            queryset: The queryset with prefetched tags.
        """
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj) -> List[str]:
        """Tag list for a post, displayed in the admin panel.

        Args:
            obj (Any): The Post object.

        Returns:
            List(str): A list of tags associated with the post.
        """
        return ", ".join(o.name for o in obj.tags.all())


class PortfolioJobsAdmin(admin.ModelAdmin):
    """Admin configuration for PortfolioJobs model."""

    list_display = ("company", "role", "start_date", "end_date", "created_at", "updated_at")


class PortfolioEducationAdmin(admin.ModelAdmin):
    """Admin configuration for PortfolioEducation model."""

    list_display = ("institution", "degree", "field_of_study", "start_date", "end_date", "created_at", "updated_at")


class PortfolioCertificationsAdmin(admin.ModelAdmin):
    """Admin configuration for PortfolioCertifications model."""

    list_display = (
        "name",
        "issuing_organization",
        "issue_date",
        "credential_id",
        "credential_url",
        "created_at",
        "updated_at",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Project)
admin.site.register(PortfolioSkills, PortfolioSkillsAdmin)
admin.site.register(PortfolioEducation, PortfolioEducationAdmin)
admin.site.register(PortfolioJobs, PortfolioJobsAdmin)
admin.site.register(PortfolioCertifications, PortfolioCertificationsAdmin)
