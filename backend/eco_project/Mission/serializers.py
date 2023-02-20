from rest_framework import serializers
from .models import Mission, CompletedMission

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class CompletedMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedMission
        fields = ['user', 'mission', 'date_completed']
