"""Template tags for rendering a tag cloud in the sidebar."""

from typing import Dict, Any
from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("portfolio_blog/tag-cloud.html", takes_context=True)
def sidebar_tag_cloud(context) -> Dict[str, Any]:
    """Returns a dictionary of tags with their respective post counts.

    Returns:
        Dict[str, Any]: A dictionary containing the tags.
    """
    request = context["request"]
    tags = Tag.objects.all()
    return {"tags": tags, "request": request}
