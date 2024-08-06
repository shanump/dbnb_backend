#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Check if the DB is running..."

    while ! nc  -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "the DB is up and running now!"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"