from rest_framework import generics, mixins
from .models import Mission, CompletedMission
from .serializers import MissionSerializer, CompletedMissionSerializer
from django.http import HttpResponse

# GET, POST/받아오거나 생성할 Mission 리스트
class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

# 미션 세부보기
class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all().order_by('id')


# 완료한 미션
class CompletedMissionList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = CompletedMissionSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            mission = CompletedMission.objects.filter(user=user_id)
            return mission
        else:
            return HttpResponse(status=401)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            reward = Mission.objects.get(pk=request.data['mission']).mileage_reward
            user.mileage += int(reward)
            user.save()
            request.data['user'] = request.user.id
            res = self.create(request, args, kwargs)
            return res
        else:
            return HttpResponse(status=401)
    
