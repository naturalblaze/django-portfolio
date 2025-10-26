"""Tests views.py for the portfolio_app app."""

import pytest
from django.urls import reverse
from django.core.cache import cache

pytestmark = pytest.mark.django_db


class TestHomeView:
    """Test suite for the HomeView."""

    def test_home_view_status_code(self, client):
        """Test that the home view returns a 200 status code."""
        response = client.get(reverse("homepage"))

        assert response.status_code == 200

    def test_home_view_template(self, client):
        """Test that the home view uses the correct template."""
        response = client.get(reverse("homepage"))

        assert "portfolio_app/index.html" in [t.name for t in response.templates]

    def test_home_view_uses_cached_wordcloud(self, client):
        """If the wordcloud image is cached, HomeView should use it from cache."""
        cache_key = "word_cloud_image"
        cache_value = "cached-image-data"
        cache.set(cache_key, cache_value, timeout=60)

        response = client.get(reverse("homepage"))
        assert response.status_code == 200
        assert response.context["wordcloud"] == cache_value

    def test_home_view_filters_by_tag(self, project_factory, client):
        """Test Home view with filter by tag."""

        response = client.get(reverse("homepage") + "?filter_field=tagx")
        assert response.status_code == 200


class TestResumeView:
    """Test suite for the ResumeView."""

    def test_resume_view_status_code(self, client):
        """Test that the resume view returns a 200 status code."""
        response = client.get(reverse("resume"))

        assert response.status_code == 200

    def test_resume_view_template(self, client):
        """Test that the resume view uses the correct template."""
        response = client.get(reverse("resume"))

        assert "portfolio_app/resume.html" in [t.name for t in response.templates]


class TestProjectsView:
    """Test suite for the ProjectsView."""

    def test_projects_view_status_code(self, client):
        """Test that the projects view returns a 200 status code."""
        response = client.get(reverse("projects_all"))

        assert response.status_code == 200

    def test_projects_view_template(self, client):
        """Test that the projects view uses the correct template."""
        response = client.get(reverse("projects_all"))

        assert "portfolio_app/project-all.html" in [t.name for t in response.templates]

    def test_projects_view_filtering(self, project_factory, client):
        """Test that the projects view filters projects by tag."""
        project1 = project_factory(title="Project 1", tags=["tag1"])
        response_tag = client.get(reverse("projects_all") + "?filter_field=tag1")
        response_title = client.get(reverse("projects_all") + "?search_field=Project+1")

        assert response_tag.status_code == 200
        assert len(response_tag.context["projects"]) == 1
        assert response_tag.context["projects"][0] == project1
        assert response_title.status_code == 200
        assert len(response_title.context["projects"]) == 1
        assert response_title.context["projects"][0] == project1

    def test_projects_view_htmx_returns_partial(self, client):
        """HTMX requests to ProjectsView should return the partial template."""
        headers = {"HTTP_HX_REQUEST": "true"}
        response = client.get(reverse("projects_all"), **headers)

        assert response.status_code == 200
        assert "portfolio_app/project-all-partial.html" in [t.name for t in response.templates]


class TestProjectView:
    """Test suite for the ProjectView."""

    def test_project_view_status_code(self, project_factory, client):
        """Test that the project view returns a 200 status code."""
        project = project_factory(slug="test-project")
        response = client.get(reverse("project_single", args=["test-project"]))

        assert response.status_code == 200

    def test_project_view_template(self, project_factory, client):
        """Test that the project view uses the correct template."""
        project = project_factory(slug="test-project")
        response = client.get(reverse("project_single", args=["test-project"]))

        assert "portfolio_app/project-single.html" in [t.name for t in response.templates]

    def test_project_view_no_project_img(self, project_factory, client):
        """Test that the project view sets a default image if none is provided."""
        project = project_factory(slug="test-project", project_img="")
        response = client.get(reverse("project_single", args=["test-project"]))

        assert response.status_code == 200
        assert response.context["project_img"] == "default-project.png"


class TestAboutView:
    """Test suite for the AboutView."""

    def test_about_view_status_code(self, portfolio_factory, client):
        """Test that the about view returns a 200 status code."""
        portfolio = portfolio_factory()
        response = client.get(reverse("about"))

        assert response.status_code == 200

    def test_about_view_template(self, portfolio_factory, client):
        """Test that the project view uses the correct template."""
        portfolio = portfolio_factory()
        response = client.get(reverse("about"))

        assert "portfolio_app/about.html" in [t.name for t in response.templates]
