from .repositories import TrainingReportRepository, DailyPainReportRepository


class TrainingReportService:
    @staticmethod
    def list_for_user(user):
        return TrainingReportRepository.list_for_user(user)


class DailyPainReportService:
    @staticmethod
    def list_for_user(user):
        return DailyPainReportRepository.list_for_user(user)
