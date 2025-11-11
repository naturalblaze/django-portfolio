"""Markdown processing template tags"""

import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(value: str) -> str:
    """Converts a string to HTML using Markdown.

    Args:
        value (str): The string to convert.

    Returns:
        str: The converted HTML string.
    """
    if not value:
        return ""

    # Use the markdown library to convert the value
    html = md.markdown(value, extensions=["extra", "codehilite", "pymdownx.emoji"])

    return html
