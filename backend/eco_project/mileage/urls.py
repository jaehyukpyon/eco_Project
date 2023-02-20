from django.urls import path
from .views import MileageCreateView

urlpatterns = [
    path('', MileageCreateView.as_view(), name='create_mileage'),
]