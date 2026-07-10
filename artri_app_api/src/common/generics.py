from rest_framework import generics, permissions


class UserScopedListCreateView(generics.ListCreateAPIView):
    """List+create view scoped to the logged-in user.

    Concrete subclasses set `serializer_class` and `service` (an object
    exposing `list_for_user(user)`).
    """
    permission_classes = [permissions.IsAuthenticated]
    service = None

    def get_queryset(self):
        return self.service.list_for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
