from src.models import Remedy


class RemedyRepository:
    @staticmethod
    def list_for_user(user):
        return Remedy.objects.filter(user=user)
