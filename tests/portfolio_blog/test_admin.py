"""Tests for admin.py"""

import pytest
from django.contrib import admin
from portfolio_blog.models import Post


@pytest.mark.django_db
def test_post_is_registered_in_admin():
    # Check that Post is registered in the admin site
    assert Post in admin.site._registry
