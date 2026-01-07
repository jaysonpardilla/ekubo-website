#!/bin/bash
set -e

echo "Starting E-Kubo application..."

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Daphne (ASGI server for Django Channels)
daphne core.core.asgi:application --bind 0.0.0.0 --port $PORT
