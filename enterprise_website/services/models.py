from django.db import models
import misaka
from django.utils.text import slugify

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(blank=True, default='')
    slug = models.SlugField(allow_unicode=True, unique=True)
    front_page = models.ImageField()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("services:single", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['title']