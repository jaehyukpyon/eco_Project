from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    
    class Meta:
        model = Member
        fields = ('username', 'password')
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }
