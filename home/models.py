from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.contrib.auth import timezone


class Post(models.Model):
    post = models.CharField(max_length=30)
    text = models.CharField(max_length=250)
    image = models.ImageField( upload_to='posts/%Y/%m/%d', blank=True)
    image2 = models.ImageField( upload_to='posts/%Y/%m/%d', blank=True)
    image3 = models.ImageField( upload_to='posts/%Y/%m/%d', blank=True)
    image4 = models.ImageField( upload_to='posts/%Y/%m/%d', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post
# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Homeimage(models.Model):
    #header = models.CharField(max_length=500)
    #text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='homeimages/%Y/%m/%d', blank=True)
    

    
    