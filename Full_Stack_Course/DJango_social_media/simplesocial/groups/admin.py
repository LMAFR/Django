from django.contrib import admin
from . import models

# Register your models here.
# The two lines below allow us to modify the model in the admin page:
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)