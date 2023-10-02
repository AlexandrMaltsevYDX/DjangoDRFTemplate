#!/bin/sh

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate

echo "Running Database populations"
python manage.py loaddata /usr/src/fixtures/db_fixture.json

exec "$@"