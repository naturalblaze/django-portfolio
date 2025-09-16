"""Models for the portfolio_blog application."""

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    """Model representing a blog post."""

    status_options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField()
    post_img = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_options, default="draft")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tags = TaggableManager()

    def get_absolute_url(self):
        """Return the URL to access a particular post instance."""
        return reverse("post_single", args=[self.slug])

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the Post model."""

        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        """String representation of the Post model.

        Returns:
            str: The title of the post.
        """
        return str(self.title)


class Project(models.Model):
    """Model representing a project."""

    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the Project model."""

        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        """String representation of the Project model.

        Returns:
            str: The title of the project.
        """
        return str(self.title)


class PortfolioSkills(models.Model):
    """Model representing a portfolio skill."""

    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency level from 1 to 10")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tags = TaggableManager()

    def clean(self):
        """Ensure proficiency is between 1 and 10."""
        if not (1 <= self.proficiency <= 10):
            raise ValueError("Proficiency must be between 1 and 10")

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the PortfolioSkills model."""

        ordering = ["-name"]
        verbose_name = "Portfolio Skill"
        verbose_name_plural = "Portfolio Skills"

    def __str__(self) -> str:
        """String representation of the PortfolioSkills model.

        Returns:
            str: The name of the skill.
        """
        return str(self.name)


class PortfolioJobs(models.Model):
    """Model representing a portfolio job."""

    company = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    description = models.TextField()
    projects = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the PortfolioJobs model."""

        ordering = ["-start_date"]
        verbose_name = "Portfolio Job"
        verbose_name_plural = "Portfolio Jobs"

    def __str__(self) -> str:
        """String representation of the PortfolioJobs model.

        Returns:
            str: The company and role of the job.
        """
        return f"{self.company} - {self.role}"


class PortfolioEducation(models.Model):
    """Model representing a portfolio education entry."""

    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the PortfolioEducation model."""

        ordering = ["-start_date"]
        verbose_name = "Portfolio Education"
        verbose_name_plural = "Portfolio Education"

    def __str__(self) -> str:
        """String representation of the PortfolioEducation model.

        Returns:
            str: The institution and degree of the education entry.
        """
        return f"{self.institution} - {self.degree}"


class PortfolioCertifications(models.Model):
    """Model representing a portfolio certification."""

    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, null=True, blank=True)
    credential_url = models.URLField(max_length=200, null=True, blank=True)
    credential_img = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the PortfolioCertifications model."""

        ordering = ["-issue_date"]
        verbose_name = "Portfolio Certification"
        verbose_name_plural = "Portfolio Certifications"

    def __str__(self) -> str:
        """String representation of the PortfolioCertifications model.

        Returns:
            str: The name of the certification.
        """
        return str(self.name)
