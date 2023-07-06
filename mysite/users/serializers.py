from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthenticationSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8)

    def validate_login(self, login):
        # try:
        #     user = User.objects.get(usernaem=login)
        # except user.DoesNotExist:
        #     return login
        # raise ValidationError("User with this username already exists")

        if User.objects.filter(username=login).count() > 0:
            raise ValidationError("User with this username already exists")
        return login
