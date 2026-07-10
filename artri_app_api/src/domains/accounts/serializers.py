from rest_framework import serializers

from src.models import User
from .services import RegistrationService


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 'birth_date', 'weight', 'height'
        ]

    def create(self, validated_data):
        return RegistrationService.register(validated_data)
