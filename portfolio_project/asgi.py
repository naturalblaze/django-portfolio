"""
ASGI config for portfolio_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from portfolio_project.settings import base

if base.env_name == "local":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings.production")

application = get_asgi_application()
