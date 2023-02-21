from rest_framework import generics
from .models import Mission, CompletedMission
from .serializers import MissionSerializer, CompletedMissionSerializer

# GET, POST/받아오거나 생성할 Mission 리스트
class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

# 미션 세부보기
class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all().order_by('id')


# 완료한 미션
class CompletedMissionCreate(generics.ListCreateAPIView):
    queryset = CompletedMission.objects.all()
    serializer_class = CompletedMissionSerializer