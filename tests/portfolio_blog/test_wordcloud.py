"""Tests wordcloud.py for the portfolio_blog app."""

import pytest
from django.contrib.staticfiles import finders
import matplotlib.font_manager as fm

from portfolio_blog.wordcloud import show_wordcloud


def test_show_wordcloud_returns_data_url(monkeypatch):
    """show_wordcloud should return a data URL string for a normal list of words."""
    # Ensure finders.find returns a real existing font path to avoid font errors
    real_font = fm.findfont(fm.FontProperties())
    monkeypatch.setattr(finders, "find", lambda path: real_font)

    data = ["django", "python", "pytest"]
    result = show_wordcloud(data)

    assert isinstance(result, str)
    assert result.startswith("data:image/png;base64,")


def test_show_wordcloud_with_empty_list(monkeypatch):
    """show_wordcloud should handle an empty list and still return a data URL or None."""
    real_font = fm.findfont(fm.FontProperties())
    monkeypatch.setattr(finders, "find", lambda path: real_font)

    result = show_wordcloud([])

    # The function should either return a data URL string or None if it cannot generate
    assert result is None or (isinstance(result, str) and result.startswith("data:image/png;base64,"))
