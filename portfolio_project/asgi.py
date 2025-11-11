"""
ASGI config for portfolio_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from portfolio_project.utils import setup_django_environment

setup_django_environment()
application = get_asgi_application()
