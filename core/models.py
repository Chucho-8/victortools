from django.db import models  # Importamos el módulo de modelos de Django
from django.contrib.auth.models import User
#  Modelo para las máquinas 
class Maquina(models.Model):
    # Definimos los tipos de máquina disponibles
    TIPO_CHOICES = [
        ('Empaquetadora', 'Empaquetadora'),
        ('Cubrebocas', 'Cubrebocas'),
    ]
    
    nombre = models.CharField(max_length=100)  # Nombre de la máquina
    #tipo = models.CharField(max_length=50)  # Tipo de máquina: empaquetadora, cubrebocas, etc.
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)  # Aquí agregamos choices
    estado = models.BooleanField(default=False)  # True = encendida, False = apagada
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente al guardar cambios
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maquinas") #

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

    def __str__(self):
        return self.nombre


#  Modelo para guardar registros o eventos 
class Registro(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    mensaje = models.TextField()  # Texto describiendo el evento
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del registro

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha}'


#  Modelo para conteo de producción (productos terminados) 
class ConteoProduccion(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)  # Número de productos terminados
    fecha = models.DateField(auto_now_add=True)  # Fecha del conteo

    class Meta:
        verbose_name = "Conteo de producción"
        verbose_name_plural = "Conteos de producción"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha} - {self.cantidad} piezas'


#  Modelo para contar activaciones de pistones 
class Piston(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre del pistón
    conteo_activaciones = models.PositiveIntegerField(default=0)  # Número de activaciones

    class Meta:
        verbose_name = "Pistón"
        verbose_name_plural = "Pistones"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_activaciones} activaciones'


#  Modelo para monitorear motores 
class Motor(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre del motor
    encendido = models.BooleanField(default=False)  # Estado del motor
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente

    class Meta:
        verbose_name = "Motor"
        verbose_name_plural = "Motores"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {"Encendido" if self.encendido else "Apagado"}'


#  Modelo para el sensor de peso 
class SensorPeso(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    peso_objetivo = models.FloatField()  # Peso deseado en gramos
    peso_actual = models.FloatField(default=0)  # Peso medido en tiempo real
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente

    class Meta:
        verbose_name = "Sensor de peso"
        verbose_name_plural = "Sensores de peso"

    def __str__(self):
        return f'{self.maquina.nombre} - Peso objetivo: {self.peso_objetivo}g'


#  Modelo para sensores ópticos (para contar productos que pasan) 
class SensorOptico(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre del sensor óptico
    conteo_detecciones = models.PositiveIntegerField(default=0)  # Conteo de detecciones

    class Meta:
        verbose_name = "Sensor óptico"
        verbose_name_plural = "Sensores ópticos"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_detecciones} detecciones'



# class Historial(models.Model):
#     maquina = models.ForeignKey('Maquina', on_delete=models.CASCADE, related_name='historiales')#A qué máquina pertenece el evento
#     #usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     evento = models.CharField(max_length=100)  # Encendido, Apagado, Producción, Error, etc.
#     cantidad_producida = models.PositiveIntegerField(null=True, blank=True)  # Solo si aplica, Cuántos productos hizo (solo para eventos de producción).
#     timestamp = models.DateTimeField(auto_now_add=True)  # Se guarda automáticamente la fecha y hora

#     class Meta:
#         verbose_name = "Historial de Máquina"
#         verbose_name_plural = "Historiales de Máquinas"
#         ordering = ['-timestamp']  # Que el más reciente salga primero

#     def __str__(self):
#         return f"{self.evento} - {self.maquina.nombre} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"



class HistorialProduccion(models.Model):
    maquina = models.ForeignKey('Maquina', on_delete=models.CASCADE, related_name='historiales')
    cantidad_producida = models.PositiveIntegerField()  # Cantidad de productos fabricados
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Fecha y hora cuando se guardó el registro
    evento = models.CharField(max_length=100, blank=True)  # Tipo de evento, opcional: 'Encendido', 'Apagado', 'Producción', etc.

    class Meta:
        verbose_name = "Historial de Producción"
        verbose_name_plural = "Historiales de Producción"

    def __str__(self):
        return f"{self.maquina.nombre} - {self.cantidad_producida} unidades - {self.fecha_hora}"