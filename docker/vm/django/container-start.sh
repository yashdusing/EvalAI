#!/bin/sh
python manage.py migrate --noinput  && \
python manage.py collectstatic --noinput  && \
uwsgi --ini /code/docker/vm/django/uwsgi.ini
