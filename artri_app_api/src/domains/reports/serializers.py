from rest_framework import serializers

from src.models import TrainingReport, DailyPainReport


class TrainingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingReport
        fields = '__all__'
        read_only_fields = ('user',)


class DailyPainReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPainReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at')
