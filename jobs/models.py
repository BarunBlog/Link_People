from django.db import models


EmpType_choises = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('self-employed', 'Self-employed'),
        ('internship', 'Internship'),
        ('seasonal', 'Seasonal')
    )


class PostJobModel(models.Model):
    Job_title = models.CharField(max_length=150, blank=False)
    Company = models.CharField(max_length=150, blank=False)
    Job_location = models.CharField(max_length=250, blank=False)
    Employee_type = models.CharField(max_length=20, blank=False, choices=EmpType_choises)
    
class PostJobPartTwoModel(models.Model):
    Description = models.TextField(blank=False)
    Add_skills = models.TextField(blank=False)
    Email_address = models.EmailField(blank=False)
