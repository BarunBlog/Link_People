import uuid
from django.db import models

from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.urls import reverse

from PIL import Image
from django.core.files.storage import default_storage as storage

from django.db import DEFAULT_DB_ALIAS

EmpType_choises = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('self-employed', 'Self-employed'),
        ('internship', 'Internship'),
        ('seasonal', 'Seasonal')
    )


class UserProfileInfo(models.Model):

    u_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    id = models.OneToOneField(
        CustomUser(),
        on_delete=models.CASCADE
    )
    # Main Info
    User_image = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    Headline = models.CharField(max_length=50, blank=False)
    Current_position = models.CharField(max_length=100, blank=True)
    Summary = models.TextField(blank=True)

    # Education
    School_or_College_or_University = models.CharField(max_length=250, blank=False)
    Degree = models.CharField(max_length=250, blank=False)
    Field_of_study = models.CharField(max_length=250, blank=False)
    Education_Start_year = models.DateField(blank=False) 
    Education_End_year = models.DateField(blank=False) 


    # Experience
    Experience_Title = models.CharField(max_length=250, blank=True)
    Employee_type = models.CharField(max_length=20, blank=True, choices=EmpType_choises)
    Company = models.CharField(max_length=250, blank=True)

    Start_year = models.DateField(blank=True, null=True)
    End_year = models.DateField(blank=True, null=True)


    # Skill
    Skill = models.TextField(blank=True)



    def save(self, *args, **kwargs):
        super(UserProfileInfo, self).save(*args, **kwargs)
        if self.User_image:
            filename = str(self.User_image.path)
            img = Image.open(filename)
            width, height = img.size  # Get dimensions

            if width > 300 and height > 300:
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

            if width > 300 and height > 300:
                img.thumbnail((300, 300), Image.ANTIALIAS)
            img.save(filename)
            '''fh = storage.open(self.User_image.name, "wb")
            format = 'png'
            img.save(fh, format)
            fh.close()'''



    def __str__(self):
        return self.Headline

    def get_absolute_url(self):
        return reverse('user_profile_info', kwargs={'pk':str(self.pk)})