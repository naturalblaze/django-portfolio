"""Configuration file for pytest to set up the testing environment."""

import os, sys
import pytest
from pytest_factoryboy import register
from .factories import PostFactory


@pytest.fixture(scope="session", autouse=True)
def set_temp_env_var():
    """Set temporary environment variables for testing."""

    base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
    sys.path.append(os.path.join(base_path))

    os.environ["SECRET_KEY"] = "test_secret_key"
    os.environ["DEBUG"] = "True"

    yield


register(PostFactory)
