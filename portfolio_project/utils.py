"""Utilities for portfolio_project project"""

import os
from pathlib import Path
from portfolio_project.settings import base


def setup_django_environment() -> None:
    """
    Sets up the Django environment for matplotlib to avoid issues in headless environments and
    configures the settings module based on the environment.
    This function should be called at the start of the application.
    """
    if base.ENV_NAME == "local":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings.production")

    base_dir = Path(__file__).resolve().parent.parent
    os.environ["MPLCONFIGDIR"] = os.path.join(base_dir, "matplotlib")
