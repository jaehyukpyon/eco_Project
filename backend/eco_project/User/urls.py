from django.urls import path
from .views import UserList, UserDetail, LoginView, LogoutView, UserCreateAPIView

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]