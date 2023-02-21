from django.urls import path
from .views import UserList, UserDetail, UserCreate, register
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView
)
urlpatterns = [
    path('', UserList.as_view(), name='user-list'), # 유저 목록을 get으로 전체 확인
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'), # 유저 목록 중 Id를 get으로 부분 확인 
    path('register/', register), #회원가입
    path('login/', TokenObtainPairView.as_view()),
]