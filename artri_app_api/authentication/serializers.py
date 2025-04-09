# authentication/serializers.py
from rest_framework import serializers
from .models import Remedy, Exercise, Training, TrainingReport, DailyPainReport

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RemedySerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedy
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class TrainingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingReport
        fields = '__all__'

class DailyPainReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPainReport
        fields = '__all__'  # ou especifique os campos que deseja incluir

