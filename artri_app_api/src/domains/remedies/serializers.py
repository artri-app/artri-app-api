from rest_framework import serializers

from src.models import Remedy


class RemedySerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedy
        fields = '__all__'
        read_only_fields = ('user',)
