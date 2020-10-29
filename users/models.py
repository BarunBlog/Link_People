from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
from PIL import Image


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    city_or_district = models.CharField(max_length=100)
    is_posted_job = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image_thumbnail = models.ImageField(upload_to='profile_pic/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.username = self.email
        self.last_login = timezone.now()
        
        super(CustomUser, self).save()

        if self.image_thumbnail:
            img = Image.open(self.image_thumbnail.path)
            width, height = img.size  # Get dimensions

            if width > 100 and height > 100:
                # keep ratio but shrink down
                img.thumbnail((width, height))

            # check which one is smaller
            if height < width:
                # make square by cutting off equal amounts left and right
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))

            elif width < height:
                # make square by cutting off bottom
                left = 0
                right = width
                top = 0
                bottom = width
                img = img.crop((left, top, right, bottom))

            if width > 100 and height > 100:
                img.thumbnail((100, 100))

            img.save(self.image_thumbnail.path)

