from django.urls import path
from .views import RegistroUsuarioAPIView, LoginUsuarioAPIView, UserProfileView

urlpatterns = [
    path('registro/', RegistroUsuarioAPIView.as_view(), name='registro'), # Ruta para registrar usuarios
    path('login/', LoginUsuarioAPIView.as_view(), name='login'),
    path('perfil/', UserProfileView.as_view(), name='user-profile'),
]
