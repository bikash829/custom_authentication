from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)