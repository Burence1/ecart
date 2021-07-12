import cloudinary
from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name=("Name of Category"))
  image = CloudinaryField('category', verbose_name=("Image"))
  parent_category=models.ForeignKey('self',limit_choices_to={'parent_category__isnull':True},on_delete=models.CASCADE,blank=True,null=True,verbose_name=("Category Parent"))

  def __str__(self):
    return self.name

class Brand(models.Model):
  name = models.CharField(max_length=100, verbose_name=("Name of Brand"))
  category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=("Category"))

  def __str__(self):
      return str(self.name)

class Product(models.Model):
  name = models.CharField(max_length=100, verbose_name=("Product Name"))
  desc = models.TextField(verbose_name=("Product Description"))
  prod_model = models.CharField(max_length=100, verbose_name=("Product Model"))
  price = models.DecimalField(decimal_places=2, max_digits=6,verbose_name=("Product Price"))
  stock_items = models.IntegerField(verbose_name=("Product Items in Stock"))
  brand = models.ForeignKey(Brand,on_delete=models.CASCADE, verbose_name=("Brand ID"))
  category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=("Category ID"))
  image = CloudinaryField('product',verbose_name=("Product  Image"), blank=True, null=True)

  def __str__(self):
    return self.name

class Image(models.Model):
  product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name="Product ID")
  front_view = CloudinaryField('front_view',verbose_name=("Product Front Image"))
  top_view = CloudinaryField('top_view',verbose_name=("Product Top Image"))
  side_view = CloudinaryField('side_view',verbose_name=("Product Side Image"))
  inner_view = CloudinaryField('inner_view',verbose_name=("Product Inner Image"))


class Comment(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=("Product ID"))
  user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=("User ID"))
  comment = models.TextField(verbose_name=("Product Comment"))
  review = models.DecimalField(decimal_places=1,max_digits=2,verbose_name=("Product Stars Review"))
