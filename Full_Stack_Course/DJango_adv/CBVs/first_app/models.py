from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

    # The method below is required by the CreateView CBV in order to change the url after creating a new school:
    def get_absolute_url(self):
        return reverse("first_app:detail", kwargs={"pk":self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# We did not add any primary key because all of the attributes could have duplicates in these models.

