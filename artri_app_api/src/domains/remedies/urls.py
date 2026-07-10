from django.urls import path

from .controllers import RemedyListCreateView

urlpatterns = [
    path('remedies/', RemedyListCreateView.as_view(), name='remedy-list-create'),
]
