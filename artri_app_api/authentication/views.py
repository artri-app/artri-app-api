from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

from .models import Remedy, Exercise, Training, TrainingReport, DailyPainReport, User
from .serializers import (
    UserRegistrationSerializer,
    RemedySerializer,
    ExerciseSerializer,
    TrainingSerializer,
    TrainingReportSerializer,
    DailyPainReportSerializer
)

# --- VIEWS PÚBLICAS ---

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    # A ROTA DE REGISTRO DEVE SER PÚBLICA
    permission_classes = [permissions.AllowAny]


# --- VIEWS PROTEGIDAS ---

class RemedyListCreateView(generics.ListCreateAPIView):
    serializer_class = RemedySerializer
    # 1. PROTEGE A ROTA: SÓ USUÁRIOS LOGADOS PODEM ACESSAR
    permission_classes = [permissions.IsAuthenticated]

    # 2. FILTRA A LISTA: MOSTRA APENAS OS REMÉDIOS DO USUÁRIO LOGADO
    def get_queryset(self):
        return Remedy.objects.filter(user=self.request.user)

    # 3. ASSOCIA O NOVO REMÉDIO AO USUÁRIO LOGADO
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TrainingReportListCreateView(generics.ListCreateAPIView):
    serializer_class = TrainingReportSerializer
    # 1. PROTEGE A ROTA
    permission_classes = [permissions.IsAuthenticated]

    # 2. FILTRA A LISTA
    def get_queryset(self):
        return TrainingReport.objects.filter(user=self.request.user)

    # 3. ASSOCIA O NOVO REGISTRO
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DailyPainReportListCreateView(generics.ListCreateAPIView):
    serializer_class = DailyPainReportSerializer
    # 1. PROTEGE A ROTA
    permission_classes = [permissions.IsAuthenticated]

    # 2. FILTRA A LISTA
    def get_queryset(self):
        return DailyPainReport.objects.filter(user=self.request.user)

    # 3. ASSOCIA O NOVO REGISTRO
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()
        params = self.request.query_params

        # Fluxo de exercícios personalizados: só exercícios com categoria definida.
        if params.get('personalized') in ('true', 'True', '1'):
            queryset = queryset.exclude(category__isnull=True).exclude(category='')

        category = params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        difficulty = params.get('difficulty')
        if difficulty:
            # O app envia 'easy'/'medium'/'hard'; o banco guarda 'Easy'/'Medium'/'Hard'.
            queryset = queryset.filter(difficulty__iexact=difficulty)

        return queryset


class TrainingListCreateView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


# --- SINAL DE RESET DE SENHA ---

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # ... (seu código de envio de email continua o mesmo)
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        "Password Reset for {title}".format(title="Some website title"),
        email_plaintext_message,
        "noreply@somehost.local",
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()