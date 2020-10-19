import uuid
from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse



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
    id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # Main Info
    User_image = models.ImageField(upload_to='profile_pic/')
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



    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('user_profile_info', kwargs={'pk':str(self.pk)})