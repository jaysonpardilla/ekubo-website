#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r core/requirements.txt

echo "Running migrations..."
cd core && python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Build complete!"
