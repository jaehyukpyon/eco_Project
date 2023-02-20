from django.urls import path
from .views import UserList, UserDetail, createUser

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('create/', createUser, name='user-create'),
]