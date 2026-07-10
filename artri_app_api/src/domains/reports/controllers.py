from src.common.generics import UserScopedListCreateView

from .serializers import TrainingReportSerializer, DailyPainReportSerializer
from .services import TrainingReportService, DailyPainReportService


class TrainingReportListCreateView(UserScopedListCreateView):
    serializer_class = TrainingReportSerializer
    service = TrainingReportService


class DailyPainReportListCreateView(UserScopedListCreateView):
    serializer_class = DailyPainReportSerializer
    service = DailyPainReportService
