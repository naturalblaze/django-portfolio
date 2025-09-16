"""Tests views.py for the portfolio_blog app."""

import pytest
from django.urls import reverse

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

        assert "portfolio_blog/index.html" in [t.name for t in response.templates]


class TestPortfolioView:
    """Test suite for the PortfolioView."""

    def test_portfolio_view_status_code(self, client):
        """Test that the portfolio view returns a 200 status code."""
        response = client.get(reverse("portfolio"))

        assert response.status_code == 200

    def test_portfolio_view_template(self, client):
        """Test that the portfolio view uses the correct template."""
        response = client.get(reverse("portfolio"))

        assert "portfolio_blog/portfolio.html" in [t.name for t in response.templates]


class TestPostsView:
    """Test suite for the PostsView."""

    def test_posts_view_status_code(self, client):
        """Test that the posts view returns a 200 status code."""
        response = client.get(reverse("posts_all"))

        assert response.status_code == 200

    def test_posts_view_template(self, client):
        """Test that the posts view uses the correct template."""
        response = client.get(reverse("posts_all"))

        assert "portfolio_blog/posts-all.html" in [t.name for t in response.templates]

    def test_posts_view_filtering(self, post_factory, client):
        """Test that the posts view filters posts by tag."""
        post1 = post_factory(title="Post 1", tags=["tag1"])
        response_tag = client.get(reverse("posts_all") + "?filter_field=tag1")
        response_title = client.get(reverse("posts_all") + "?search_field=Post+1")

        assert response_tag.status_code == 200
        assert len(response_tag.context["posts"]) == 1
        assert response_tag.context["posts"][0] == post1
        assert response_title.status_code == 200
        assert len(response_title.context["posts"]) == 1
        assert response_title.context["posts"][0] == post1


class TestPostView:
    """Test suite for the PostView."""

    def test_post_view_status_code(self, post_factory, client):
        """Test that the post view returns a 200 status code."""
        post = post_factory(slug="test-post")
        response = client.get(reverse("post_single", args=["test-post"]))

        assert response.status_code == 200

    def test_post_view_template(self, post_factory, client):
        """Test that the post view uses the correct template."""
        post = post_factory(slug="test-post")
        response = client.get(reverse("post_single", args=["test-post"]))

        assert "portfolio_blog/post-single.html" in [t.name for t in response.templates]

    def test_post_view_no_post_img(self, post_factory, client):
        """Test that the post view sets a default image if none is provided."""
        post = post_factory(slug="test-post", post_img="")
        response = client.get(reverse("post_single", args=["test-post"]))

        assert response.status_code == 200
        assert response.context["post_img"] == "default-post.png"
