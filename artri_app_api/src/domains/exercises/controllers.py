from rest_framework import generics

from src.models import Training

from .serializers import ExerciseSerializer, TrainingSerializer
from .services import ExerciseService


class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return ExerciseService.list_filtered(self.request.query_params)


class TrainingListCreateView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
