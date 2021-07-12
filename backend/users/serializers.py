from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','username','email','bio','avatar']
    extra_kwargs = {
        'password': {'write_only': True, }
    }

    def create(self, validated_data):
      newUser = User(
          email=validated_data['email'],
          username=validated_data['username']
      )
      newUser.set_password(validated_data['password'])
      newUser.save()
      return newUser