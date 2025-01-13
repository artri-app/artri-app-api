from django.urls import path
from .views import LoginView
from django.urls import path, include

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]