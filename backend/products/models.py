import cloudinary
from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name=("Name of Category"))
  image = CloudinaryField('category')
  parent_category=models.ForeignKey('self',limit_choices_to={'parent_category__isnull':True},on_delete=models.CASCADE,blank=True,null=True,verbose_name=("Category Parent"))

  def __str__(self):
    return self.name

class Brand(models.Model):
  name = models.CharField(max_length=100, verbose_name=("Name of Brand"))
