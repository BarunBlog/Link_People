from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
from PIL import Image
from django.core.files.storage import default_storage as storage
from django.db import DEFAULT_DB_ALIAS

from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


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

        if self.image_thumbnail:

            img = Image.open(self.image_thumbnail)
   
            #file_type = self.image_thumbnail.file.content_type
            format = img.format

            outputIoStream = BytesIO()

            if format=='PNG':
                rgb_img = img.convert('RGB')
                imageTemporaryResized = rgb_img.resize( (100,100) )
                imageTemporaryResized.save(outputIoStream, format='JPEG', quality=90)
                outputIoStream.seek(0)
                self.image_thumbnail = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" %self.image_thumbnail.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
            
            else:
                imageTemporaryResized = img.resize( (100,100) )
                imageTemporaryResized.save(outputIoStream, format='PNG', quality=90)
                outputIoStream.seek(0)
                self.image_thumbnail = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.png" %self.image_thumbnail.name.split('.')[0], 'image/png', sys.getsizeof(outputIoStream), None)         
        
        super(CustomUser, self).save(*args, **kwargs)

        '''if self.image_thumbnail:
            img = Image.open(self.image_thumbnail)
            width, height = img.size  # Get dimensions

            if width > 100 and height > 100:
                # keep ratio but shrink down
                img.thumbnail((width, height), Image.ANTIALIAS)

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
                img.thumbnail((100, 100), Image.ANTIALIAS)

            fh = storage.open(self.image_thumbnail.name, "wb")
            format = 'png'
            img.save(fh, format)
            fh.close()'''

