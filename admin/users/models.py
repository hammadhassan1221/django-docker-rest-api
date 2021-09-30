from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
