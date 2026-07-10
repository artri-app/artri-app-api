from src.common.generics import UserScopedListCreateView

from .serializers import RemedySerializer
from .services import RemedyService


class RemedyListCreateView(UserScopedListCreateView):
    serializer_class = RemedySerializer
    service = RemedyService
