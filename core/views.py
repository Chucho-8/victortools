from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Maquina, HistorialProduccion
from .serializers import MaquinaSerializer, HistorialProduccionSerializer
from django.utils.dateparse import parse_date
from django.http import HttpResponse

# Vista para la raíz
def home(request):
    return HttpResponse("¡Bienvenido a la aplicación de monitoreo!")

class MaquinaListAPIView(APIView):
    def get(self, request):
        maquinas = Maquina.objects.all()  # Obtener todas las máquinas
        serializer = MaquinaSerializer(maquinas, many=True)  # Serializarlas
        return Response(serializer.data)  # Devolverlas como respuesta

    def post(self, request):
            serializer = MaquinaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import generics
# from .models import Maquina
# from .serializers import MaquinaSerializer

# class MaquinaListAPIView(generics.ListAPIView):
#     queryset = Maquina.objects.all()
#     serializer_class = MaquinaSerializer

#De dorma automática con el RetrieveUpdateDestroyAPIView
# class MaquinaDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Maquina.objects.all()
#     serializer_class = MaquinaSerializer
#De froma "manual"
class MaquinaDetailAPIView(APIView): #creamos otra vista para trabajar con una sóla máquina, por si la queremos ediatr, 
    def get(self, request, pk):
        maquina = get_object_or_404(Maquina, pk=pk)
        serializer = MaquinaSerializer(maquina)
        return Response(serializer.data)

    def put(self, request, pk):
        maquina = get_object_or_404(Maquina, pk=pk)
        serializer = MaquinaSerializer(maquina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Buscamos la máquina por su clave primaria (pk)
        maquina = get_object_or_404(Maquina, pk=pk)

        # Guardamos el estado anterior (antes de actualizar)
        estado_anterior = maquina.estado

        # Preparamos el serializer para actualizar solo los campos enviados (partial=True)
        serializer = MaquinaSerializer(maquina, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Guardamos los cambios en la máquina
            maquina_actualizada = serializer.save()

            # Obtenemos el nuevo estado después de actualizar
            nuevo_estado = maquina_actualizada.estado

            # Verificamos si el estado cambió (de encendido a apagado o viceversa)
            if estado_anterior != nuevo_estado:
                from .models import HistorialProduccion  # Importamos aquí para evitar bucles

                # Definimos qué tipo de evento es
                evento = "Encendido" if nuevo_estado else "Apagado"

                # Creamos un nuevo registro en el historial
                HistorialProduccion.objects.create(
                    maquina=maquina_actualizada,    # Máquina relacionada
                    cantidad_producida=0,           # Inicialmente 0, hasta conectar con datos reales
                    evento=evento                   # Guardamos si fue encendido o apagado
                )

            # Devolvemos los datos actualizados al cliente
            return Response(serializer.data)
        
        # Si hubo errores de validación, los devolvemos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        maquina = get_object_or_404(Maquina, pk=pk)
        maquina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class HistorialProduccionListAPIView(APIView):
    """
    Lista los historiales de producción.
    Puedes filtrar por máquina (id) y por fecha (YYYY-MM-DD).
    """
    def get(self, request):
        # Tomamos filtros de la query: /api/historiales/?maquina=1&fecha=2025-04-28
        maquina_id = request.query_params.get('maquina')
        fecha = request.query_params.get('fecha')

        historiales = HistorialProduccion.objects.all()

        if maquina_id:
            historiales = historiales.filter(maquina_id=maquina_id)

        if fecha:
            fecha_obj = parse_date(fecha)
            if fecha_obj:
                historiales = historiales.filter(fecha_hora__date=fecha_obj)
            else:
                return Response({'error': 'Formato de fecha inválido (usa YYYY-MM-DD)'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = HistorialProduccionSerializer(historiales, many=True)
        return Response(serializer.data)

