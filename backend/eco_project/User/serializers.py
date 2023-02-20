from rest_framework import serializers
from .models import User

# User 생성을 위한 serializer
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'account']
        extra_kwargs = {'password': {'write_only': True}}

# User 목록을 확인하기 위한 serializer
class ViewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# class CustomTokenSerializer(serializers.ModelSerializer):
