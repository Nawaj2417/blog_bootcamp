# blog/models.py

from django.db import models
from django.utils.text import slugify
# import uuid
# auto slug field
from autoslug import AutoSlugField
# category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)



    def __str__(self):
        return self.name

# for blog
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')    #for category
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
