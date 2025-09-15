"""Tests for markdown_processing.py"""

import pytest
from portfolio_blog.template_tags.markdown_processing import markdown


@pytest.mark.parametrize(
    "input_text,expected_html_fragment",
    [
        ("**bold**", "<strong>bold</strong>"),
        ("# Heading", "<h1>Heading</h1>"),
        ("", ""),
        ("`code`", "<code>code</code>"),
        (":smile:", ":smile:"),  # emoji extension may not render actual emoji without config
    ],
)
def test_markdown_filter(input_text, expected_html_fragment):
    html = markdown(input_text)
    assert expected_html_fragment in html
