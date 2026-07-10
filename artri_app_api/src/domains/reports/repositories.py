from src.models import TrainingReport, DailyPainReport


class TrainingReportRepository:
    @staticmethod
    def list_for_user(user):
        return TrainingReport.objects.filter(user=user)


class DailyPainReportRepository:
    @staticmethod
    def list_for_user(user):
        return DailyPainReport.objects.filter(user=user)
