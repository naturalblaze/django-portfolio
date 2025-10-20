#!/usr/bin/env bash

# Collect Static content
python manage.py collectstatic --noinput

# Migrate database tables
python manage.py migrate --noinput

# Start server
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 portfolio_project.wsgi:application
