from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandAPI(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class Product_FilterAPI(ListAPIView):
    serializer_class = ProductIDSerializer

    def get_queryset(self):
      num = self.kwargs['num']
      if num == 1:
          return Product.objects.filter(category__in=[2, 3, 4, 5])
      elif num == 6:
          return Product.objects.filter(category__in=[7, 8, 9, 10])
      elif num == 11:
          return Product.objects.filter(category__in=[12, 13, 14, 15])
      elif num == 16:
          return Product.objects.filter(category__in=[17, 18, 19, 20])
      else:
          return Product.objects.filter(category=num)

class GetProductById(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id=id)

class GetPicturesByProductId(ListAPIView):
    serializer_class = PictureIDSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductImage.objects.filter(product_id=product_id)

class GetCommentsByProductId(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Comment.objects.filter(product=product_id)

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer