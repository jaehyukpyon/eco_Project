from rest_framework import generics
from .models import Member
from .serializers import CreateUserSerializer, ViewUserSerializer
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# User 전체 목록 보기
class UserList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = ViewUserSerializer

# User Id 개별 목록 보기
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = ViewUserSerializer

# User 목록 생성
class UserCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = CreateUserSerializer

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    account = random.randint(10,1000000)
    if not username or not password:
        return Response({'error': 'Please provide both username and password.'})
    if Member.objects.filter(username=username).exists():
        return Response({'error': 'User with this username already exists.'})
    user = Member.objects.create_user(username=username, password=password, account=account)
    return Response({'message': 'User created successfully.'})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Invalid username or password.'})
    refresh = RefreshToken.for_user(user)
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    })

        