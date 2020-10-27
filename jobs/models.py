import uuid
from django.db import models

from django.urls import reverse
from django.utils import timezone

from django.contrib.auth import get_user_model


EmpType_choises = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('self-employed', 'Self-employed'),
        ('internship', 'Internship'),
        ('seasonal', 'Seasonal')
    )


class PostJobModel(models.Model):
    Job_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    Job_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    Job_title = models.CharField(max_length=150, blank=False)
    Company = models.CharField(max_length=150, blank=False)
    Job_location = models.CharField(max_length=250, blank=False)
    Employee_type = models.CharField(max_length=20, blank=False, choices=EmpType_choises)
    
    Date_posted = models.DateField(default=timezone.now)
    Is_approved = models.BooleanField(default=False)

    Description = models.TextField(blank=False)
    Add_skills = models.TextField(blank=False)
    
    def __str__(self):
        return self.Job_title

    def get_absolute_url(self):
        return reverse('jobs_details', kwargs={'pk':str(self.pk)})



class ApplicationModel(models.Model):
    Job = models.ForeignKey(
        PostJobModel,
        on_delete=models.CASCADE,
    )
    Job_title = models.CharField(max_length=150, blank=False)
    Applicant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.Job_title
