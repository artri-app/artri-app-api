from django.urls import path
from .views import (
    RemedyListCreateView,
    ExerciseListCreateView,
    TrainingListCreateView,
    TrainingReportListCreateView,
    DailyPainReportListCreateView,
    DailySleepReportListCreateView,
    DailySwellingReportListCreateView,
    DailyFatigueReportListCreateView,
    UserRegistrationView,
)
from django.urls import path, include

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('remedies/', RemedyListCreateView.as_view(), name='remedy-list-create'),
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('trainings/', TrainingListCreateView.as_view(), name='training-list-create'),
    path('training-reports/', TrainingReportListCreateView.as_view(), name='training-report-list-create'),
    path('daily-pain-reports/', DailyPainReportListCreateView.as_view(), name='daily-pain-report-list-create'),
    path('daily-sleep-reports/', DailySleepReportListCreateView.as_view(), name='daily-sleep-report-list-create'),
    path('daily-swelling-reports/', DailySwellingReportListCreateView.as_view(), name='daily-swelling-report-list-create'),
    path('daily-fatigue-reports/', DailyFatigueReportListCreateView.as_view(), name='daily-fatigue-report-list-create'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
