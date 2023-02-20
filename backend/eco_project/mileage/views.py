from rest_framework import generics
from .models import Mileage
from .serializers import MileageSerializer

# POST 기능 (마일리지 획득)
class MileageList(generics.ListCreateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer    

# GEt, UPDATE, PUT기능 
class MileageDetail(generics.RetrieveUpdateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer

