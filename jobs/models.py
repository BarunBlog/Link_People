import uuid
from django.db import models

from django.urls import reverse
from django.utils import timezone


EmpType_choises = (
        ('full-time', 'Full-time'),
        ('entry-level', 'Entry-level'),
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
    Job_title = models.CharField(max_length=150, blank=False)
    Company = models.CharField(max_length=150, blank=False)
    Job_location = models.CharField(max_length=250, blank=False)
    Employee_type = models.CharField(max_length=20, blank=False, choices=EmpType_choises)
    
    Date_posted = models.DateField(default=timezone.now)
    Is_approved = models.BooleanField(default=False)

    Description = models.TextField(blank=False)
    Add_skills = models.TextField(blank=False)
    Email_address = models.EmailField(blank=False)
    
    def __str__(self):
        return self.Job_title

    def get_absolute_url(self):
        return reverse('jobs_details', kwargs={'pk':str(self.pk)})
    
    
