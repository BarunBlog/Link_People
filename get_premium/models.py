import uuid
from django.db import models
from django.utils import timezone

from django.shortcuts import reverse

class PremiumBlog(models.Model):
    Blog_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    Author = models.CharField(max_length=150, blank=False)
    Title = models.CharField(max_length=150, blank=False)
    Blog_Cover = models.ImageField(upload_to='premium_images/', blank=True)
    Date_Posted = models.DateField(default=timezone.now)
    Description = models.TextField(blank=False)


    class Meta:
        permissions = [
            ('special_status', 'Can read all blogs')
        ]


    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk':str(self.pk)})


