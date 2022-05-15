#!/bin/sh

python manage.py collectstatic --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 

