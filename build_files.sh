#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Create superuser if needed (optional, uncomment if needed)
# python manage.py createsuperuser --noinput

echo "Build completed successfully!"