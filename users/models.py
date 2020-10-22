from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    city_or_district = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.username = self.email
        self.last_login = timezone.now()
        super(CustomUser, self).save()
