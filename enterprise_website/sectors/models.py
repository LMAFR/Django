from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse
# Create your models here.

class Sector(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    front_page = models.ImageField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sectors:single", kwargs={"slug": self.slug})
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
