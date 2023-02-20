from django.db import models
from django.contrib.auth.models import User

class Mileage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    mileage = models.PositiveIntegerField(default=0)
    current_mileage = models.PositiveIntegerField(default=0)