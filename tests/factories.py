"""Factories for tests."""

import factory
from django.contrib.auth.models import User
from portfolio_blog.models import (
    Portfolio,
    Project,
    ResumeSkills,
    ResumeJobs,
    ResumeEducation,
    ResumeCertifications,
)


class PortfolioFactory(factory.django.DjangoModelFactory):
    """Portfolio factory for tests."""

    class Meta:
        """Meta class for PortfolioFactory."""

        model = Portfolio
        skip_postgeneration_save = True

    first_name = "x"
    last_name = "x"
    email = "test@email.com"
    introduction = "x"
    professional_experience = "x"


class UserFactory(factory.django.DjangoModelFactory):
    """User factory for tests."""

    class Meta:
        """Meta class for UserFactory."""

        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class ProjectFactory(factory.django.DjangoModelFactory):
    """Project factory for tests."""

    class Meta:
        """Meta class for ProjectFactory."""

        model = Project
        skip_postgeneration_save = True

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    project_img = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create: str, extracted: list, **kwargs):
        """Add tags to the post instance.

        Args:
            create (str): _indicates if instance is created_
            extracted (list): _list of tags to add_
        """
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)

        else:
            self.tags.add("default-tag")


class ResumeSkillsFactory(factory.django.DjangoModelFactory):
    """ResumeSkills factory for tests."""

    class Meta:
        """Meta class for ResumeSkillsFactory."""

        model = ResumeSkills
        skip_postgeneration_save = True

    name = "x"
    proficiency = 8

    @factory.post_generation
    def tags(self, create: str, extracted: list, **kwargs):
        """Add tags to the post instance.

        Args:
            create (str): _indicates if instance is created_
            extracted (list): _list of tags to add_
        """
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)

        else:
            self.tags.add("default-tag")


class ResumeJobsFactory(factory.django.DjangoModelFactory):
    """ResumeJobs factory for tests."""

    class Meta:
        """Meta class for ResumeJobsFactory."""

        model = ResumeJobs
        skip_postgeneration_save = True

    company = "x"
    role = "x"
    description = "x"
    projects = "x"
    start_date = "2020-01-01"


class ResumeEducationFactory(factory.django.DjangoModelFactory):
    """ResumeEducation factory for tests."""

    class Meta:
        """Meta class for ResumeEducationFactory."""

        model = ResumeEducation
        skip_postgeneration_save = True

    institution = "x"
    degree = "x"
    field_of_study = "x"
    start_date = "2020-01-01"
    end_date = "2024-01-01"


class ResumeCertificationsFactory(factory.django.DjangoModelFactory):
    """ResumeCertifications factory for tests."""

    class Meta:
        """Meta class for ResumeCertificationsFactory."""

        model = ResumeCertifications
        skip_postgeneration_save = True

    name = "x"
    issuing_organization = "x"
    issue_date = "2020-01-01"
    credential_id = "x"
    credential_url = "http://example.com/credential/x"
    credential_img = "x"
