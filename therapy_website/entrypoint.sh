#!/bin/sh
set -e

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec "$@"
