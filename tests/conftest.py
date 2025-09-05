"""Configuration file for pytest to set up the testing environment."""

from pytest_factoryboy import register
from .factories import PostFactory

register(PostFactory)
