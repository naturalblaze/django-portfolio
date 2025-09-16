"""Tests models.py for the portfolio_blog app."""

import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    """Test suite for the Post model."""

    def test_str_method(self, post_factory):
        """Test the __str__ method of the Post model."""
        post = post_factory(title="Test Post")

        assert post.__str__() == "Test Post"

    def test_add_tags(self, post_factory):
        """Test adding tags to a Post instance."""
        post = post_factory(title="Test Post", tags=["test-tag"])

        assert post.tags.count() == 1
        assert post.tags.first().name == "test-tag"

    def test_get_absolute_url(self, post_factory):
        """Test the get_absolute_url method of the Post model."""
        post = post_factory(slug="test-post")

        assert post.get_absolute_url() == "/posts/test-post/"


class TestPortfolioSkillsModel:
    """Test suite for the PortfolioSkills model."""

    def test_str_method(self, portfolio_skills_factory):
        """Test the __str__ method of the PortfolioSkills model."""
        skill = portfolio_skills_factory(name="Python")

        assert skill.__str__() == "Python"

    def test_add_tags(self, portfolio_skills_factory):
        """Test adding tags to a PortfolioSkills instance."""
        skill = portfolio_skills_factory(name="Python", tags=["programming"])

        assert skill.tags.count() == 1
        assert skill.tags.first().name == "programming"

    def test_proficiency_range(self):
        """Test that the proficiency field is within the valid range."""
        from portfolio_blog.models import PortfolioSkills

        instance = PortfolioSkills(name="Invalid Skill", proficiency=11)
        with pytest.raises(ValueError):
            instance.full_clean()


class TestPortfolioJobsModel:
    """Test suite for the PortfolioJobs model."""

    def test_str_method(self, portfolio_jobs_factory):
        """Test the __str__ method of the PortfolioJobs model."""
        job = portfolio_jobs_factory(company="Tech Corp", role="Developer")

        assert job.__str__() == "Tech Corp - Developer"


class TestPortfolioEducationModel:
    """Test suite for the PortfolioEducation model."""

    def test_str_method(self, portfolio_education_factory):
        """Test the __str__ method of the PortfolioEducation model."""
        education = portfolio_education_factory(institution="University", degree="BSc Computer Science")

        assert education.__str__() == "University - BSc Computer Science"


class TestPortfolioCertificationsModel:
    """Test suite for the PortfolioCertifications model."""

    def test_str_method(self, portfolio_certifications_factory):
        """Test the __str__ method of the PortfolioCertifications model."""
        certification = portfolio_certifications_factory(name="Django Certification")

        assert certification.__str__() == "Django Certification"
