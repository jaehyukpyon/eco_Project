from rest_framework import generics,mixins
from .models import Mileage
from .serializers import MileageSerializer
from django.http import HttpResponse


# GET POST 기능 (마일리지 획득)
class MileageList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = MileageSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            mile = Mileage.objects.filter(user=user_id)
            return mile
        else:
            return HttpResponse(status=401)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            user.mileage += int(request.data.get('mileage'))
            user.save()
            request.POST._mutable = True
            request.POST['user'] = request.user.id
            return self.create(request, args, kwargs)
        else:
            return HttpResponse(status=401)
