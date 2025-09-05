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
