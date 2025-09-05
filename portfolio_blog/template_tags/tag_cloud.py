"""Template tags for rendering a tag cloud in the sidebar."""

from typing import Dict, Any
from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("portfolio_blog/tag-cloud.html")
def sidebar_tag_cloud() -> Dict[str, Any]:
    """Returns a dictionary of tags with their respective post counts.

    Returns:
        Dict[str, Any]: A dictionary containing the tags.
    """
    tags = Tag.objects.all()
    return {"tags": tags}
