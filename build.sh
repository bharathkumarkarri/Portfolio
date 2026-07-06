#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py shell -c "
from django.contrib.auth.models import User

print('Checking superuser...')

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='Admin@123'
    )
    print('Superuser created!')
else:
    print('Superuser already exists!')
"