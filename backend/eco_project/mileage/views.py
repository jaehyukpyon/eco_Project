from rest_framework import generics
from .models import Mileage
from .serializers import MileageSerializer

class MileageCreateView(generics.CreateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
