"""Django models for portfolio_blog application."""

from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    """Model representing a blog post.

    Args:
        models (models.Model): Django model base class.

    Returns:
        models.Model: Post model instance
    """
    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    content = models.TextField()
    status = models.CharField(max_length=10, choices=status_options, default='draft')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
