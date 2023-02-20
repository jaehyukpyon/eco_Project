from django.urls import path
from .views import MileageList, MileageDetail

urlpatterns = [
    path('', MileageList.as_view(), name='mileage'),
    path('<int:pk>/', MileageDetail.as_view()),
]