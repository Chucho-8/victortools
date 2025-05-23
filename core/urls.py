from django.urls import path
from .views import MaquinaListAPIView, MaquinaDetailAPIView, HistorialProduccionListAPIView, SenalesListAPIView, SenalDetailAPIView

urlpatterns = [
    path('maquinas/', MaquinaListAPIView.as_view(), name='lista-maquinas'),
    path('maquinas/<int:pk>/', MaquinaDetailAPIView.as_view(), name='maquina-detail'),
    path('historiales/', HistorialProduccionListAPIView.as_view(), name='historiales-list'),
    path('senales/', SenalesListAPIView.as_view()),
    path('senales/<int:pk>/', SenalDetailAPIView.as_view()),
]