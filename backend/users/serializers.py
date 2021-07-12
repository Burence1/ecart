from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','username','email','bio','avatar','password','is_verified']
    extra_kwargs = {
        'password': {'write_only': True, }
    }

    def create(self, validated_data):
      regUser = User(
          email=validated_data['email'],
          username=validated_data['username']
      )
      regUser.set_password(validated_data['password'])
      regUser.save()
      return regUser

class CartSerializer(serializers.ModelSerializer):
  
  product_name = serializers.CharField(source='product.name')
  product_price = serializers.DecimalField(decimal_places=2, max_digits=6, source='product.price')
  product_model = serializers.CharField(source='product.prod_model')
  product_image = serializers.ImageField(source='product.image')

  class Meta:
      model = Cart
      exclude = []


class CartQTYSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = []
