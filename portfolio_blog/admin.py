"""Admin configuration for portfolio_blog app."""

from typing import List
from django.contrib import admin
from .models import Portfolio, Project, ResumeSkills, ResumeEducation, ResumeJobs, ResumeCertifications


class PortfolioAdmin(admin.ModelAdmin):
    """Admin configuration for Portfolio model."""

    list_display = (
        "first_name",
        "last_name",
        "email",
        "linkedin_url",
        "github_url",
        "portfolio_img",
        "introduction",
        "professional_experience",
    )


class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for Project model, to show additional fields in admin panel."""

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
        """Tag list for a project, displayed in the admin panel.

        Args:
            obj (Any): The Project object.

        Returns:
            List(str): A list of tags associated with the project.
        """
        return ", ".join(o.name for o in obj.tags.all())


class ResumeSkillsAdmin(admin.ModelAdmin):
    """Admin configuration for ResumeSkills model."""

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
        """Tag list for a project, displayed in the admin panel.

        Args:
            obj (Any): The Project object.

        Returns:
            List(str): A list of tags associated with the project.
        """
        return ", ".join(o.name for o in obj.tags.all())


class ResumeJobsAdmin(admin.ModelAdmin):
    """Admin configuration for ResumeJobs model."""

    list_display = ("company", "role", "start_date", "end_date", "created_at", "updated_at")


class ResumeEducationAdmin(admin.ModelAdmin):
    """Admin configuration for ResumeEducation model."""

    list_display = ("institution", "degree", "field_of_study", "start_date", "end_date", "created_at", "updated_at")


class ResumeCertificationsAdmin(admin.ModelAdmin):
    """Admin configuration for ResumeCertifications model."""

    list_display = (
        "name",
        "issuing_organization",
        "issue_date",
        "credential_id",
        "credential_url",
        "created_at",
        "updated_at",
    )


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ResumeSkills, ResumeSkillsAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
admin.site.register(ResumeJobs, ResumeJobsAdmin)
admin.site.register(ResumeCertifications, ResumeCertificationsAdmin)
