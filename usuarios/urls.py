from django.urls import path
from .views import RegistroUsuarioAPIView, LoginUsuarioAPIView, UserProfileView
from .views import RegistroUsuarioAPIView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro/', RegistroUsuarioAPIView.as_view(), name='registro'), # Ruta para registrar usuarios
    #path('login/', LoginUsuarioAPIView.as_view(), name='login'),
    path('perfil/', UserProfileView.as_view(), name='user-profile'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
