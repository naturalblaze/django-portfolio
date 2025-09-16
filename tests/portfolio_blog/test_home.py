"""home page tests."""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    """Test suite for the home page."""

    homepage = reverse("homepage")

    def test_homepage_url(self, client):
        """Test the homepage URL."""
        url = self.homepage
        response = client.get(url)

        assert response.status_code == 200
        assertTemplateUsed(response, "portfolio_blog/index.html")

    def test_post_htmx_fragment(self, client):
        """Test HTMX request for post list fragment."""
        headers = {"HTTP_HX_REQUEST": "true"}
        response = client.get(self.homepage, **headers)

        assertTemplateUsed(response, "portfolio_blog/post-list-elements.html")
