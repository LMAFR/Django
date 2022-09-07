from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self) -> str:
        # Taking the username field define by default in auth.models.User, we can get a string representation of the user as follows:
        return "@{}".format(self.username)