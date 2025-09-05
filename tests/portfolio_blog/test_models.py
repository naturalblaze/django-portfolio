"""models.py tests for the blog app."""

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
