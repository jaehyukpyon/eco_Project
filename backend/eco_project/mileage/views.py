from rest_framework import generics,mixins
from .models import Mileage
from rest_framework.decorators import api_view
from .serializers import MileageSerializer
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.response import Response

# GET POST 기능 (마일리지 획득)
class MileageList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = MileageSerializer

    def get_queryset(self):
        return Mileage.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
            mile = Mileage.objects.filter(user=user_id)
            return self.list(request, args, kwargs)
        else:
            return HttpResponse(status=401)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            user.mileage += int(request.data.get('mileage'))
            user.save()
            return self.create(request, args, kwargs)
        else:
            return HttpResponse(status=401)
<<<<<<< HEAD
=======

# GEt, UPDATE, PUT기능 
class MileageDetail(generics.RetrieveUpdateAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer

    

>>>>>>> f5a3831877deb3fda39fdbba78dec478e280468b
