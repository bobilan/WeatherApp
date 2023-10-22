#!/bin/ash

echo "Apply migrations"
python manage.py makemigrations --settings=config.settings.dev
python manage.py migrate --settings=config.settings.dev

exec "$@"