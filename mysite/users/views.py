from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers

# Create your views here.


@api_view(["POST"])
def authorization_view(request):
    """ Достаем данные """
    login = request.data.get('login')
    password = request.data.get('password')

    """ Аутентификация """
    user = authenticate(username=login, password=password)

    """ Берем тоокен """
    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        return Response(data={"token": token.key})

    return Response(data={"message": "Authorization failed"}, status=status.HTTP_401_UNAUTHORIZED)





@api_view(["POST"])
def register_view(request):
    serializer = serializers.AuthenticationSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        login = serializer.validated_data.get('login')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=login, password=password)

        return Response(data={"message: Successfully registered"})

    return Response(data={'message: Something went wrong'})