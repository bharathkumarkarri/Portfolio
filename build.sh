#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        'Pavan',
        'bharath.karri23@gmail.com',
        'Pavan@1234'
    )
"