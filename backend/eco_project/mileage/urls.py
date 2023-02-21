from django.urls import path
from .views import MileageList, MileageDetailView

urlpatterns = [
    path('', MileageList.as_view(), name='mileage'),
    path('<int:pk>/', MileageDetailView.as_view()),
]