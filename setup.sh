#!/bin/bash

# Install dependencies
pip install setuptools
pip install -r requirements.txt

# Run the Django migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear

# Run the Django application
python manage.py runserver