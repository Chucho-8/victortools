# usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Maquina  
#from core.models import Maquina  
from core.serializers import MaquinaSerializer  # si está en core


# Este serializer se encarga de convertir los datos de User a JSON y viceversa
class UserSerializer(serializers.ModelSerializer):

    # Esta clase Meta le dice a Django qué modelo y qué campos vamos a usar
    class Meta:
        model = User  # Modelo que vamos a serializar (el que ya trae Django)
        fields = ('id', 'username', 'password', 'email')  # Campos que queremos incluir
        extra_kwargs = {
            'password': {'write_only': True},  # Que la contraseña no se lea al hacer GET
            'email': {'required': True}         # Que el email sea obligatorio
        }

    # Método que define cómo crear un nuevo usuario
    def create(self, validated_data):
        # Creamos un nuevo usuario con username y email
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        # Usamos set_password para que guarde la contraseña encriptada
        user.set_password(validated_data['password'])
        user.save()  # Guardamos el usuario en la base de datos
        return user  # Retornamos el usuario creado
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    maquinas = MaquinaSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()  # Esto mostrará el username en vez del ID

    class Meta:
        model = UserProfile
        fields = ['user', 'maquinas']
