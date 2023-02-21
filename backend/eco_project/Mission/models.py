from django.db import models
from member.models import Member

# 미션 목록
class Mission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    mileage_reward = models.PositiveIntegerField()

# 완료한 미션 목록
class CompletedMission(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)