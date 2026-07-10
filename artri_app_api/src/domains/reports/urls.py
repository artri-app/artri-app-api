from django.urls import path

from .controllers import TrainingReportListCreateView, DailyPainReportListCreateView

urlpatterns = [
    path('training-reports/', TrainingReportListCreateView.as_view(), name='training-report-list-create'),
    path('daily-pain-reports/', DailyPainReportListCreateView.as_view(), name='daily-pain-report-list-create'),
]
