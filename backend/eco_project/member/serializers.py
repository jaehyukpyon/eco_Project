from rest_framework import serializers
from .models import Member

# User 생성을 위한 serializer
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

# User 목록을 확인하기 위한 serializer
class ViewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'username', 'account', 'mileage']


# class CustomTokenSerializer(serializers.ModelSerializer):
