"""Factories for tests."""

import factory
from django.contrib.auth.models import User
from portfolio_blog.models import Post


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
