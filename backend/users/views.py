from django.shortcuts import render
from .serializers import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
import jwt
import datetime
from .models import *
from rest_framework import viewsets

# Create your views here.
class RegisterView(APIView):
  serializer_class = UserSerializer
  def post(self, request, format=None):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

class LoginView(APIView):
  def post(self, request):
      username = request.data['username']
      password = request.data['password']
      user = User.objects.filter(username=username).first()
      if user is None:
          raise AuthenticationFailed('User not found!')
      if not user.check_password(password):
          raise AuthenticationFailed('Incorrect password!')
      if password is None:
          raise AuthenticationFailed('Input password found!')

      payload = {
          'id': user.id,
          'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
          'iat': datetime.datetime.utcnow()
      }

      token = jwt.encode(payload, 'secret', algorithm='HS256')
      print(token)
      response = Response()

      response.set_cookie(key='jwt', value=token, httponly=False)
      response.data = {
          'jwt': token
      }
      return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Invalid')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Invalid')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': "success"
        }
        return response