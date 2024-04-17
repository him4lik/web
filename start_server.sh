#!/bin/bash
python3 manage.py makemigrations --merge --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
exec python manage.py runserver 0.0.0.0:8001
