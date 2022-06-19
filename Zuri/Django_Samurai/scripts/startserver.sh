#!/bin/bash
source ./Ninja/bin/activate
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
