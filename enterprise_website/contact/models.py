from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False,default='')
    
    def __str__(self) -> str:
        return self.issue

    def get_absolute_url(self):
        return reverse("home")