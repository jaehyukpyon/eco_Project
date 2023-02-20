from django.db import models
from django.contrib.auth.models import User

# 미션 목록
class Mission(models.Model):
    user = models.ForeignKey('auth.User', related_name='missions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    mileage_reward = models.PositiveIntegerField(default=0)

# 완료한 미션 목록
class CompletedMission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)