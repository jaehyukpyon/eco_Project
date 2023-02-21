from django.contrib import admin
from .models import Mileage

# Register your models here.
@admin.register(Mileage)
class MileageAdmin(admin.ModelAdmin):
    pass