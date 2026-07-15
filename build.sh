#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

# python manage.py shell <<EOF
# from django.contrib.auth.models import User

# # Delete existing admin user
# User.objects.filter(username="admin").delete()

# # Create new admin user
# User.objects.create_superuser(
#     username="admin",
#     email="admin@example.com",
#     password="Admin@123"
# )

# print("✅ Admin user created successfully.")
# EOF