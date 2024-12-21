#!/bin/bash

rm -rf media
sleep 10

python manage.py makemigrations
python manage.py migrate
# загрузка начальных данных
python manage.py loaddata initial_data.json
# регистрация админа и пользователя
python manage.py init_admin
python manage.py init_user
# запуск сервера
python manage.py runserver 0.0.0.0:8000