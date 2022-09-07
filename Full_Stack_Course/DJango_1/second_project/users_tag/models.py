from pyexpat import model
from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=264, unique=False)
    lname = models.CharField(max_length=264, unique=False)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.email
# Don't forget to migrate them!
# python manage.py migrate
# python manage.py makemigrations users_tag
# python manage.py migrate