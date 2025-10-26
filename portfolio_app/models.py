"""Models for the portfolio_app application."""

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager


class Portfolio(models.Model):
    """Model representing portfolio person"""

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    github_url = models.URLField(max_length=200, null=True, blank=True)
    portfolio_img = models.ImageField(upload_to="portfolio_app/about/", null=True, blank=True)
    introduction = models.TextField()
    professional_experience = models.TextField()
    total_visits = models.PositiveIntegerField(default=0)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the Portfolio model."""

        verbose_name = "Portfolio"

    def clean(self):
        """Ensure only one instance of Portfolio exists."""
        if Portfolio.objects.exists() and self.pk != Portfolio.objects.first().pk:  # pylint: disable=no-member
            super().clean()
            raise ValidationError("Only one instance of Portfolio model is allowed.")

    def __str__(self) -> str:
        """String representation of the Portfolio model.

        Returns:
            str: The first and last name of the project.
        """
        return str(self.first_name + " " + self.last_name)


class Project(models.Model):
    """Model representing a blog project."""

    status_options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_author")
    content = models.TextField()
    project_img = models.ImageField(upload_to="portfolio_app/projects/", null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_options, default="draft")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tags = TaggableManager()

    def get_absolute_url(self):
        """Return the URL to access a particular project instance."""
        return reverse("project_single", args=[self.slug])

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


class ResumeSkills(models.Model):
    """Model representing a resume skill."""

    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        help_text="Proficiency level from 1 to 10", validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    skill_img = models.ImageField(upload_to="portfolio_app/skills/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tags = TaggableManager()

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the ResumeSkills model."""

        ordering = ["-name"]
        verbose_name = "Resume Skill"
        verbose_name_plural = "Resume Skills"

    def __str__(self) -> str:
        """String representation of the ResumeSkills model.

        Returns:
            str: The name of the skill.
        """
        return str(self.name)


class ResumeJobs(models.Model):
    """Model representing a resume job."""

    company = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    description = models.TextField()
    projects = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the ResumeJobs model."""

        ordering = ["-start_date"]
        verbose_name = "Resume Job"
        verbose_name_plural = "Resume Jobs"

    def __str__(self) -> str:
        """String representation of the ResumeJobs model.

        Returns:
            str: The company and role of the job.
        """
        return f"{self.company} - {self.role}"


class ResumeEducation(models.Model):
    """Model representing a resume education entry."""

    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the ResumeEducation model."""

        ordering = ["-start_date"]
        verbose_name = "Resume Education"
        verbose_name_plural = "Resume Education"

    def __str__(self) -> str:
        """String representation of the ResumeEducation model.

        Returns:
            str: The institution and degree of the education entry.
        """
        return f"{self.institution} - {self.degree}"


class ResumeCertifications(models.Model):
    """Model representing a resume certification."""

    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, null=True, blank=True)
    credential_url = models.URLField(max_length=200, null=True, blank=True)
    credential_img = models.ImageField(upload_to="portfolio_app/certifications/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for the ResumeCertifications model."""

        ordering = ["-issue_date"]
        verbose_name = "Resume Certification"
        verbose_name_plural = "Resume Certifications"

    def __str__(self) -> str:
        """String representation of the ResumeCertifications model.

        Returns:
            str: The name of the certification.
        """
        return str(self.name)
