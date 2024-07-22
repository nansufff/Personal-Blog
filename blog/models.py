from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return self.caption


class author(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    def full_name(self):
        return f"{self.fname} {self.lname}"
    def __str__(self):
        return self.full_name()


class blogpost(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=350)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(author,on_delete=models.SET_NULL,null=True,related_name="posts")
    tags=models.ManyToManyField(tag)
    def __str__(self):
        return self.title