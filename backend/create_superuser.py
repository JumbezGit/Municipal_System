#!/usr/bin/env python
"""Script to create a super admin user"""
import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'municipal_tax.settings')
django.setup()

from tax_app.models import User

# Create superuser
email = 'jumbez@email.com'
password = 'jumbez@12345'

try:
    # Check if user already exists
    if User.objects.filter(email=email).exists():
        print(f'User with email {email} already exists!')
    else:
        User.objects.create_superuser(email, password)
        print(f'Super admin created successfully!')
        print(f'Email: {email}')
        print(f'Password: {password}')
except Exception as e:
    print(f'Error creating super admin: {e}')
