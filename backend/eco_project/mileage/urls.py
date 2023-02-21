from django.urls import path
from .views import MileageList

urlpatterns = [
    path('', MileageList.as_view(), name='mileage'),
]