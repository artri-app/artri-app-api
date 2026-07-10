from rest_framework import generics, permissions

from src.models import User
from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    # A ROTA DE REGISTRO DEVE SER PÚBLICA
    permission_classes = [permissions.AllowAny]
