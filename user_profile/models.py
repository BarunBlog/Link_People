import uuid
from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

class UserProfileMainInfo(models.Model):

    u_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    user_image = models.ImageField(upload_to='profile_pic/')
    headline = models.CharField(max_length=50, blank=False)
    current_position = models.CharField(max_length=100, blank=True)
    aboutYourself = models.CharField(max_length=400, blank=True)



    def __str__(self):
        return self.u_id

    def get_absolute_url(self):
        return reverse('user_profile_main_info', kwargs={'pk':str(self.pk)})




class UserProfileEducation(models.Model):
    u_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    School_or_College_or_University = models.CharField(max_length=250, blank=False)
    Degree = models.CharField(max_length=250, blank=False)
    Field_of_study = models.CharField(max_length=250, blank=False)
    Start_year = models.DateField(blank=False) 
    Endt_year = models.DateField(blank=False) 


    def __str__(self):
        return self.u_id

    def get_absolute_url(self):
        return reverse('user_profile_education', kwargs={'pk':str(self.pk)})


EmpType_choises = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('self-employed', 'Self-employed'),
        ('internship', 'Internship'),
        ('seasonal', 'Seasonal')
    )

class UserProfileExperience(models.Model):
    u_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    Title = models.CharField(max_length=250, blank=False)
    Employee_type = models.CharField(max_length=20, blank=True, choices=EmpType_choises)
    Company = models.CharField(max_length=250, blank=False)

    Start_year = models.DateField(blank=False) 
    Endt_year = models.DateField(blank=False) 


    def __str__(self):
        return self.u_id

    def get_absolute_url(self):
        return reverse('user_profile_experience', kwargs={'pk':str(self.pk)})



class UserProfileSkill(models.Model):
    u_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    Skill = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.u_id

    def get_absolute_url(self):
        return reverse('user_profile_experience', kwargs={'pk':str(self.pk)})