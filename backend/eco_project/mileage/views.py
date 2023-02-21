from rest_framework import generics
from .models import Mileage
from rest_framework.decorators import api_view
from .serializers import MileageSerializer
from django.http import HttpResponse


# POST 기능 (마일리지 획득)
class MileageList(generics.ListCreateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            user.mileage += int(request.data.get('mileage'))
            user.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)

# GEt, UPDATE, PUT기능 
class MileageDetail(generics.RetrieveUpdateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer

    

