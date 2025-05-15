from rest_framework import serializers
from .models import Maquina, HistorialProduccion

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'  # Incluir todos los campos del modelo

class HistorialProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialProduccion
        fields = '__all__'