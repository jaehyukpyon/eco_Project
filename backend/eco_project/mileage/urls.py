from django.urls import path
<<<<<<< HEAD
from .views import MileageList

urlpatterns = [
    path('', MileageList.as_view(), name='mileage'),
=======
from .views import MileageList, MileageDetailView

urlpatterns = [
    path('', MileageList.as_view(), name='mileage'),
    path('<int:pk>/', MileageDetailView.as_view()),
>>>>>>> f5a3831877deb3fda39fdbba78dec478e280468b
]