"""Factory for creating Post instances for testing purposes."""

import random
import factory
from factory import fuzzy
from factory.faker import faker
from django.contrib.auth.models import User
from portfolio_blog.models import Post

FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    """Factory for creating Post instances."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for PostFactory."""

        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=6)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="nb")[0]  # Default author for factory

    @factory.lazy_attribute
    def content(self):
        """Create a longer content with multiple paragraphs."""
        x = ""
        for _ in range(0, 5):
            x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return x

    status = fuzzy.FuzzyChoice(choices=["draft", "published"])

    @factory.post_generation
    def tags(self, create: str, extracted: list, **kwargs):  # pylint: disable=unused-argument
        """Add tags to the post instance.

        Args:
            create (str): _indicates if instance is created_
            extracted (list): _list of tags to add_
        """
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tags.add(tag)
        else:
            for tag in random.sample(["django", "python", "blog", "factory", "test"], random.randint(1, 3)):
                self.tags.add(tag)
