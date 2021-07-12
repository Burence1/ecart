from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = []

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []

class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []

class PictureIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        return Comment.objects.create(**validated_data)