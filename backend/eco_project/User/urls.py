from django.urls import path
from .views import UserList, UserDetail, createUser
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('create/', createUser, name='user-create'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]