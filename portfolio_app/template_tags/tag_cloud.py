"""Template tags for rendering a tag cloud in the sidebar."""

from typing import Dict, Any
from django import template
from taggit.models import Tag
from portfolio_app.models import Project

register = template.Library()


@register.inclusion_tag("portfolio_app/tag-cloud.html", takes_context=True)
def sidebar_tag_cloud(context) -> Dict[str, Any]:
    """Returns a dictionary of tags for published projects.

    Returns:
        Dict[str, Any]: A dictionary containing the tags.
    """
    request = context["request"]
    published_project_ids = Project.objects.filter(status="published").values_list(  # pylint: disable=no-member
        "id", flat=True
    )
    tags = Tag.objects.filter(taggit_taggeditem_items__object_id__in=published_project_ids).distinct()

    return {"tags": tags, "request": request}
