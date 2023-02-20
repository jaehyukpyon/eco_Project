from django.urls import path
from .views import UserList, UserDetail, UserCreate

urlpatterns = [
    path('', UserList.as_view(), name='user-list'), # 유저 목록을 get으로 전체 확인
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'), # 유저 목록 중 Id를 get으로 부분 확인 
    path('create/', UserCreate.as_view(), name='user_create'), #회원가입
]