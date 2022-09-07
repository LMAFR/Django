from django.contrib import admin
from first_app.models import AccessRecord, Webpage, Topic

# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)

# Remember to create a superuser to access the databases in the /admin tag:
# python manage.py createsuperuser