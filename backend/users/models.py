from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

#user information
class User(AbstractUser):
  username = models.CharField(max_length=30,unique=True)
  email = models.EmailField(unique=True)
  is_verified = models.BooleanField(default=False)
  avatar = CloudinaryField('avatar')
  bio = models.TextField()

  REQUIRED_FIELDS=[]
  
  def __str__(self):
    return str(self.username)

#user address info
class Address(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='product ID')
  address1 = models.CharField(max_length=50)
  address2 = models.CharField(max_length=50)

#user wishlist
class Wishlist(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user ID')
  product = models.ForeignKey('products.Product',on_delete=models.CASCADE,verbose_name='product ID')

#user cart
class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user ID')
  product = models.ForeignKey('products.Product',on_delete=models.CASCADE,verbose_name='product ID')
  quantity = models.IntegerField(default=1)
