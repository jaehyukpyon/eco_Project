from rest_framework import generics
from .models import User
from .serializers import CreateUserSerializer, ViewUserSerializer

# User 전체 목록 보기
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ViewUserSerializer

# User Id 개별 목록 보기
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ViewUserSerializer

# User 목록 생성
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer