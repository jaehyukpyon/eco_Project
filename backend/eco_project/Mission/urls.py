from django.urls import path
from .views import MissionList, MissionDetail, CompletedMissionCreate

urlpatterns = [
    path('', MissionList.as_view()),
    path('<int:pk>/', MissionDetail.as_view()),
    path('completed/create/', CompletedMissionCreate.as_view(), name='completed-mission-create'),
]