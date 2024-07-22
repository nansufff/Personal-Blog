from django.db import models

# Create your models here.
class blogpost(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True)