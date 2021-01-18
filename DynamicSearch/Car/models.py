from django.db import models
from django.utils.text import slugify
from time import time


def gen_slug(slug):
    new_slug = slugify(slug)
    return new_slug + '-' + str(int(time()))




class Car(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(max_length=1000)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)
