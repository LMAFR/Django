from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.

admin.site.register(Comment)
admin.site.register(Post)