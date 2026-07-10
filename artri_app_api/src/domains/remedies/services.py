from .repositories import RemedyRepository


class RemedyService:
    @staticmethod
    def list_for_user(user):
        return RemedyRepository.list_for_user(user)
