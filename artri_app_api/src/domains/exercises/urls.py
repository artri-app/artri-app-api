from django.urls import path

from .controllers import ExerciseListCreateView, TrainingListCreateView

urlpatterns = [
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('trainings/', TrainingListCreateView.as_view(), name='training-list-create'),
]
