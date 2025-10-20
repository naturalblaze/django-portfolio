"""Tests models.py for the portfolio_blog app."""

import pytest

pytestmark = pytest.mark.django_db


class TestPortfolioModel:
    """Test suite for the Portfolio model."""

    def test_str_method(self, portfolio_factory):
        """Test the __str__ method of the Portfolio model."""
        portfolio = portfolio_factory(first_name="John", last_name="Doe")

        assert portfolio.__str__() == "John Doe"

    def test_clean_enforces_single_instance(self, portfolio_factory):
        """Ensure Portfolio.clean() raises ValidationError when a second instance is created."""
        from django.core.exceptions import ValidationError
        from portfolio_blog.models import Portfolio

        # Create the first (allowed) instance
        first = portfolio_factory(first_name="Alice", last_name="Smith")

        # Build a second instance without saving
        second = Portfolio(first_name="Bob", last_name="Jones", introduction="x", professional_experience="y")

        with pytest.raises(ValidationError):
            second.full_clean()


class TestProjectModel:
    """Test suite for the Project model."""

    def test_str_method(self, project_factory):
        """Test the __str__ method of the Project model."""
        project = project_factory(title="Test Project")

        assert project.__str__() == "Test Project"

    def test_add_tags(self, project_factory):
        """Test adding tags to a Project instance."""
        project = project_factory(title="Test Project", tags=["test-tag"])

        assert project.tags.count() == 1
        assert project.tags.first().name == "test-tag"

    def test_get_absolute_url(self, project_factory):
        """Test the get_absolute_url method of the Project model."""
        project = project_factory(slug="test-project")

        assert project.get_absolute_url() == "/projects/test-project/"


class TestResumeSkillsModel:
    """Test suite for the ResumeSkills model."""

    def test_str_method(self, resume_skills_factory):
        """Test the __str__ method of the ResumeSkills model."""
        skill = resume_skills_factory(name="Python")

        assert skill.__str__() == "Python"

    def test_add_tags(self, resume_skills_factory):
        """Test adding tags to a ResumeSkills instance."""
        skill = resume_skills_factory(name="Python", tags=["programming"])

        assert skill.tags.count() == 1
        assert skill.tags.first().name == "programming"

    def test_proficiency_range(self):
        """Test that the proficiency field is within the valid range."""
        from django.core.exceptions import ValidationError
        from portfolio_blog.models import ResumeSkills

        instance = ResumeSkills(name="Invalid Skill", proficiency=11)
        with pytest.raises(ValidationError):
            instance.full_clean()


class TestResumeJobsModel:
    """Test suite for the ResumeJobs model."""

    def test_str_method(self, resume_jobs_factory):
        """Test the __str__ method of the ResumeJobs model."""
        job = resume_jobs_factory(company="Tech Corp", role="Developer")

        assert job.__str__() == "Tech Corp - Developer"


class TestResumeEducationModel:
    """Test suite for the ResumeEducation model."""

    def test_str_method(self, resume_education_factory):
        """Test the __str__ method of the ResumeEducation model."""
        education = resume_education_factory(institution="University", degree="BSc Computer Science")

        assert education.__str__() == "University - BSc Computer Science"


class TestResumeCertificationsModel:
    """Test suite for the ResumeCertifications model."""

    def test_str_method(self, resume_certifications_factory):
        """Test the __str__ method of the ResumeCertifications model."""
        certification = resume_certifications_factory(name="Django Certification")

        assert certification.__str__() == "Django Certification"
