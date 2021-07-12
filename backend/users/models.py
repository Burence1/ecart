from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  username = models.CharField(max_length=30,unique=True)
  email = models.EmailField(unique=True)
  is_verified = models.BooleanField(default=False)
  avatar = models.ImageField()

  REQUIRED_FIELDS=[]
  
  def __str__(self):
    return str(self.username)