from django.db import models
# The line below will allow us to add urls with words instead  of the typical primary keys:
from django.utils.text import slugify
# Allow us to add markdown text and links
import misaka
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
# Create your models here.
# The line below returns the current user session
User = get_user_model()
# The line below allow us to use template tags recorded under the related_name argument. One example is in posts/templates/posts/post_list.html
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    # We will add a description that, by default, will be empty ('')
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False, default='',blank=True)
    member = models.ManyToManyField(User,through='GroupMember')

    def __str__(self) -> str:
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']
    

class GroupMember(models.Model):

    group = models.ForeignKey(Group, related_name="membership", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        unique_together = ('group','user')
    