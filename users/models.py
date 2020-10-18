from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    country = models.CharField(max_length=100)
    city_or_district = models.CharField(max_length=100)

    username = models.CharField(max_length=150, blank=True, unique=False)