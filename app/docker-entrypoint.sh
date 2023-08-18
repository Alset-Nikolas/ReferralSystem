#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Create admin"
python manage.py createsuperuser --phone=$DJANGO_SUPERUSER_PHONE --noinput || echo "admin already created"

echo "Apply database static"
python manage.py collectstatic --noinput

echo "start server"
gunicorn app.wsgi:application -w 2 -b :8000 --timeout 120 
exec "$@"
