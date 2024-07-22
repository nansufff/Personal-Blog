from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class author(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()


class blogpost(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True)
    content=models.TextField(validators=[MinLengthValidator(10)])

