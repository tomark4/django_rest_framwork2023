from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    email = models.EmailField(unique=True)
    website = models.TextField(blank=True, null=True)
    twitter = models.CharField(max_length=255,blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []