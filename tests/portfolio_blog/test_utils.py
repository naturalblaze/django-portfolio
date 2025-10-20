"""Tests utils.py for the portfolio_blog app."""


def test_get_project_dependencies_empty():
    """get_project_dependencies should return an empty dict when there are no projects."""
    from portfolio_blog.utils import get_project_dependencies

    dependencies = get_project_dependencies("bad_path")
    assert isinstance(dependencies, dict)
    assert len(dependencies) == 0
