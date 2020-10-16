from django.contrib.auth.models import AbstractUser
from django.db import models

role_choises = (
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('job seeker', 'Job Seeker'),
    )

class CustomUser(AbstractUser):
    country = models.CharField(max_length=100)
    city_or_district = models.CharField(max_length=100)

    account_role = models.CharField(max_length=12, choices=role_choises)