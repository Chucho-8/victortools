from django.db import models  # Importamos el módulo de modelos de Django

# --- Modelo para las máquinas ---
class Maquina(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la máquina (NO funciona como filtro directamente en admin, pero sí puede buscarse)
    tipo = models.CharField(max_length=50)  # Tipo de máquina (puede funcionar como filtro en el admin si lo defines en list_filter)
    estado = models.BooleanField(default=False)  # Estado encendida/apagada (funciona muy bien como filtro: True/False)
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Última actualización automática (generalmente no se usa como filtro)

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

    def __str__(self):
        return self.nombre


# --- Modelo para guardar registros o eventos ---
class Registro(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (funciona como filtro en admin)
    mensaje = models.TextField()  # Mensaje del registro (NO es ideal para filtro, mejor para búsqueda)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de creación (sí puede filtrarse por rango de fechas en el admin)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha}'


# --- Modelo para conteo de producción (productos terminados) ---
class ConteoProduccion(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (funciona como filtro)
    cantidad = models.PositiveIntegerField(default=0)  # Cantidad de productos (normalmente no se usa como filtro porque sería demasiado específico)
    fecha = models.DateField(auto_now_add=True)  # Fecha de producción (ideal para filtrar por día, mes o año en admin)

    class Meta:
        verbose_name = "Conteo de producción"
        verbose_name_plural = "Conteos de producción"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha} - {self.cantidad} piezas'


# --- Modelo para contar activaciones de pistones ---
class Piston(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (funciona como filtro)
    nombre = models.CharField(max_length=50)  # Nombre del pistón (podrías usarlo como filtro, pero en general se usa más para búsqueda)
    conteo_activaciones = models.PositiveIntegerField(default=0)  # Número de activaciones (NO ideal como filtro)

    class Meta:
        verbose_name = "Pistón"
        verbose_name_plural = "Pistones"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_activaciones} activaciones'


# --- Modelo para monitorear motores ---
class Motor(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (filtro posible)
    nombre = models.CharField(max_length=50)  # Nombre del motor (usado más para búsquedas que para filtros)
    encendido = models.BooleanField(default=False)  # Estado del motor (excelente para filtro: Encendido/Apagado)
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Última actualización automática (normalmente no como filtro)

    class Meta:
        verbose_name = "Motor"
        verbose_name_plural = "Motores"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {"Encendido" if self.encendido else "Apagado"}'


# --- Modelo para el sensor de peso ---
class SensorPeso(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (se puede usar como filtro)
    peso_objetivo = models.FloatField()  # Peso deseado (no es común filtrarlo porque pueden ser muchos valores)
    peso_actual = models.FloatField(default=0)  # Peso real (no práctico como filtro)
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Última actualización (no como filtro)

    class Meta:
        verbose_name = "Sensor de peso"
        verbose_name_plural = "Sensores de peso"

    def __str__(self):
        return f'{self.maquina.nombre} - Peso objetivo: {self.peso_objetivo}g'


# --- Modelo para sensores ópticos ---
class SensorOptico(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  # Máquina relacionada (ideal como filtro)
    nombre = models.CharField(max_length=50)  # Nombre del sensor óptico (más para búsquedas que para filtros)
    conteo_detecciones = models.PositiveIntegerField(default=0)  # Conteo de productos detectados (no como filtro)

    class Meta:
        verbose_name = "Sensor óptico"
        verbose_name_plural = "Sensores ópticos"

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_detecciones} detecciones'
