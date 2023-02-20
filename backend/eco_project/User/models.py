from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    account = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        verbose_name='User'
        verbose_name_plural = 'Users'

