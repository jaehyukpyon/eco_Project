from django.db import models
from member.models import Member

class Mileage(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE) 
    activity = models.CharField(max_length=100) # 마일리지 활동 내역
    date = models.DateTimeField(auto_now_add=True) # 마일리지 날짜 
    mileage = models.IntegerField(default=0) # 유저가 보유중인 총 마일리지
    current_mileage = models.IntegerField(default=0) # 획득한, 사용할 마일리지 값

    def update_mileage(self):
        self.mileage += self.current_mileage
        self.save()