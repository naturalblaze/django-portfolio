"""Tests admin.py for the portfolio_app app."""

import pytest
from django.contrib import admin
from portfolio_app.models import Project

pytestmark = pytest.mark.django_db


class TestProjectAdmin:
    """Test suite for the ProjectAdmin class."""

    def test_list_display(self):
        """Test that the list_display attribute is correctly set."""
        project_admin = admin.site._registry[Project]
        expected_fields = ("title", "subtitle", "slug", "author", "status", "tag_list", "created_at", "updated_at")

        assert Project in admin.site._registry
        assert project_admin.list_display == expected_fields

    def test_tag_list_method(self, project_factory):
        """Test the tag_list method of ProjectAdmin."""
        project = project_factory(tags=["tag1", "tag2"])
        project_admin = admin.site._registry[Project]
        tags = project_admin.tag_list(project)

        assert tags == "tag1, tag2"

    def test_get_queryset_method(self, project_factory):
        """Test the get_queryset method of ProjectAdmin."""
        project = project_factory(tags=["tag1", "tag2"])
        project_admin = admin.site._registry[Project]
        request = None  # Mock request object, not used in this test
        queryset = project_admin.get_queryset(request)

        assert queryset.count() == 1
        assert queryset.first() == project


class TestResumeSkillsAdmin:
    """Test suite for the ResumeSkillsAdmin class."""

    def test_list_display(self):
        """Test that the list_display attribute is correctly set."""
        from portfolio_app.models import ResumeSkills

        skills_admin = admin.site._registry[ResumeSkills]
        expected_fields = ("name", "proficiency", "tag_list", "created_at", "updated_at")

        assert ResumeSkills in admin.site._registry
        assert skills_admin.list_display == expected_fields

    def test_tag_list_method(self, resume_skills_factory):
        """Test the tag_list method of ResumeSkillsAdmin."""
        skill = resume_skills_factory(tags=["skill1", "skill2"])
        from portfolio_app.models import ResumeSkills

        skills_admin = admin.site._registry[ResumeSkills]
        tags = skills_admin.tag_list(skill)

        assert tags == "skill1, skill2"

    def test_get_queryset_method(self, resume_skills_factory):
        """Test the get_queryset method of ResumeSkillsAdmin."""
        skill = resume_skills_factory(tags=["skill1", "skill2"])
        from portfolio_app.models import ResumeSkills

        skills_admin = admin.site._registry[ResumeSkills]
        request = None  # Mock request object, not used in this test
        queryset = skills_admin.get_queryset(request)

        assert queryset.count() == 1
        assert queryset.first() == skill
