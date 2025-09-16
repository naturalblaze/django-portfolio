"""Tests admin.py for the portfolio_blog app."""

import pytest
from django.contrib import admin
from portfolio_blog.models import Post

pytestmark = pytest.mark.django_db


class TestPostAdmin:
    """Test suite for the PostAdmin class."""

    def test_list_display(self):
        """Test that the list_display attribute is correctly set."""
        post_admin = admin.site._registry[Post]
        expected_fields = ("title", "subtitle", "slug", "author", "status", "tag_list", "created_at", "updated_at")

        assert Post in admin.site._registry
        assert post_admin.list_display == expected_fields

    def test_tag_list_method(self, post_factory):
        """Test the tag_list method of PostAdmin."""
        post = post_factory(tags=["tag1", "tag2"])
        post_admin = admin.site._registry[Post]
        tags = post_admin.tag_list(post)

        assert tags == "tag1, tag2"

    def test_get_queryset_method(self, post_factory):
        """Test the get_queryset method of PostAdmin."""
        post = post_factory(tags=["tag1", "tag2"])
        post_admin = admin.site._registry[Post]
        request = None  # Mock request object, not used in this test
        queryset = post_admin.get_queryset(request)

        assert queryset.count() == 1
        assert queryset.first() == post


class TestPortfolioSkillsAdmin:
    """Test suite for the PortfolioSkillsAdmin class."""

    def test_list_display(self):
        """Test that the list_display attribute is correctly set."""
        from portfolio_blog.models import PortfolioSkills

        skills_admin = admin.site._registry[PortfolioSkills]
        expected_fields = ("name", "proficiency", "tag_list", "created_at", "updated_at")

        assert PortfolioSkills in admin.site._registry
        assert skills_admin.list_display == expected_fields

    def test_tag_list_method(self, portfolio_skills_factory):
        """Test the tag_list method of PortfolioSkillsAdmin."""
        skill = portfolio_skills_factory(tags=["skill1", "skill2"])
        from portfolio_blog.models import PortfolioSkills

        skills_admin = admin.site._registry[PortfolioSkills]
        tags = skills_admin.tag_list(skill)

        assert tags == "skill1, skill2"

    def test_get_queryset_method(self, portfolio_skills_factory):
        """Test the get_queryset method of PortfolioSkillsAdmin."""
        skill = portfolio_skills_factory(tags=["skill1", "skill2"])
        from portfolio_blog.models import PortfolioSkills

        skills_admin = admin.site._registry[PortfolioSkills]
        request = None  # Mock request object, not used in this test
        queryset = skills_admin.get_queryset(request)

        assert queryset.count() == 1
        assert queryset.first() == skill
