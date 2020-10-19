from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    country = models.CharField(max_length=100)
    city_or_district = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.username = self.email
        self.last_login = timezone.now()
        super(CustomUser, self).save()
