"""Factories for tests."""

import factory
from django.contrib.auth.models import User
from portfolio_blog.models import (
    Post,
    Project,
    PortfolioSkills,
    PortfolioJobs,
    PortfolioEducation,
    PortfolioCertifications,
)


class UserFactory(factory.django.DjangoModelFactory):
    """User factory for tests."""

    class Meta:
        """Meta class for UserFactory."""

        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    """Post factory for tests."""

    class Meta:
        """Meta class for PostFactory."""

        model = Post
        skip_postgeneration_save = True

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    post_img = "x"
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


class ProjectFactory(factory.django.DjangoModelFactory):
    """Project factory for tests."""

    class Meta:
        """Meta class for ProjectFactory."""

        model = Project
        skip_postgeneration_save = True

    title = "x"
    description = "x"
    url = "http://example.com"


class PortfolioSkillsFactory(factory.django.DjangoModelFactory):
    """PortfolioSkills factory for tests."""

    class Meta:
        """Meta class for PortfolioSkillsFactory."""

        model = PortfolioSkills
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


class PortfolioJobsFactory(factory.django.DjangoModelFactory):
    """PortfolioJobs factory for tests."""

    class Meta:
        """Meta class for PortfolioJobsFactory."""

        model = PortfolioJobs
        skip_postgeneration_save = True

    company = "x"
    role = "x"
    description = "x"
    projects = "x"
    start_date = "2020-01-01"


class PortfolioEducationFactory(factory.django.DjangoModelFactory):
    """PortfolioEducation factory for tests."""

    class Meta:
        """Meta class for PortfolioEducationFactory."""

        model = PortfolioEducation
        skip_postgeneration_save = True

    institution = "x"
    degree = "x"
    field_of_study = "x"
    start_date = "2020-01-01"
    end_date = "2024-01-01"


class PortfolioCertificationsFactory(factory.django.DjangoModelFactory):
    """PortfolioCertifications factory for tests."""

    class Meta:
        """Meta class for PortfolioCertificationsFactory."""

        model = PortfolioCertifications
        skip_postgeneration_save = True

    name = "x"
    issuing_organization = "x"
    issue_date = "2020-01-01"
    credential_id = "x"
    credential_url = "http://example.com/credential/x"
    credential_img = "x"
