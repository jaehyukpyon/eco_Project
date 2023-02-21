from django.db import models
from member.models import Member

class Mileage(models.Model):
    user = models.ForeignKey(Member, default=0,on_delete=models.CASCADE, related_name="+") 
    activity = models.CharField(max_length=100) # 마일리지 활동 내역
    date = models.DateTimeField(auto_now_add=True) # 마일리지 날짜 
    mileage = models.IntegerField(default=0) # 획득한 마일리지
