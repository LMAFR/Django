from django.contrib import admin
from users_tag.models import Users

# Register your models here.

admin.site.register(Users)

# Remember to create a superuser to access the databases in the /admin tag:
# python manage.py createsuperuser