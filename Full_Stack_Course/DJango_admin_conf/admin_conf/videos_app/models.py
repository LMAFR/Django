from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    # The string representation provided in the next two lines of code is what makes the different elements of the databases in admin to appear 
    # as such string representation (in this case a title we previously stored) instead of simply object(1), object(2), etc.
    def __str__(self) -> str:
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name