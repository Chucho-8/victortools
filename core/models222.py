from django.db import models  # Importamos el módulo de modelos de Django

# --- Modelo para las máquinas ---
class Maquina(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la máquina, hasta 100 caracteres
    tipo = models.CharField(max_length=50)  # Tipo de máquina: empaquetadora, cubrebocas, etc.
    estado = models.BooleanField(default=False)  # True = encendida, False = apagada
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se guarda el objeto

    def __str__(self):
        return self.nombre  # Para que en el admin aparezca el nombre de la máquina


#  Modelo para guardar registros o eventos 
class Registro(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  
    # Relación: cada registro pertenece a una máquina
    # Si se elimina la máquina, también se eliminan sus registros (CASCADE)
    
    mensaje = models.TextField()  # Texto describiendo el evento (por ejemplo: "Se encendió la máquina")
    fecha = models.DateTimeField(auto_now_add=True)  # Guarda automáticamente la fecha/hora al crear el registro

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha}'  # Mostrar máquina y fecha del registro


#  Modelo para conteo de producción (productos terminados) 
class ConteoProduccion(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)  #Te indica que esta conectando esa tabla con otra, en este caso: maquina
    cantidad = models.PositiveIntegerField(default=0)  # Número de productos terminados ##No funciona como filtro
    fecha = models.DateField(auto_now_add=True)  # Fecha en que se produjo esa cantidad ##Funciona como filtro

    def __str__(self):
        return f'{self.maquina.nombre} - {self.fecha} - {self.cantidad} piezas'  # Ejemplo de cómo se verá en admin


#  Modelo para contar activaciones de pistones 
class Piston(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre para identificar el pistón (ej: Pistón 1)
    conteo_activaciones = models.PositiveIntegerField(default=0)  # Número de veces que el pistón se ha activado

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_activaciones} activaciones'


#  Modelo para monitorear motores 
class Motor(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre del motor (ej: Motor Principal)
    encendido = models.BooleanField(default=False)  # True = encendido, False = apagado
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente al guardar cambios

    def __str__(self):
        # Muestra si el motor está encendido o apagado en el panel de admin
        return f'{self.maquina.nombre} - {self.nombre} - {"Encendido" if self.encendido else "Apagado"}'


# Modelo para el sensor de peso 
class SensorPeso(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    peso_objetivo = models.FloatField()  # Peso deseado en gramos (por ejemplo 100g, 200g)
    peso_actual = models.FloatField(default=0)  # Lo que realmente mide el sensor en tiempo real
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente

    def __str__(self):
        return f'{self.maquina.nombre} - Peso objetivo: {self.peso_objetivo}g'


# Modelo para sensores ópticos (para contar productos que pasan) 
class SensorOptico(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)  # Nombre para identificar el sensor
    conteo_detecciones = models.PositiveIntegerField(default=0)  # Cuántos productos ha detectado
    #PositiveIntegerField: Guarda el número entero positivo

    def __str__(self):
        return f'{self.maquina.nombre} - {self.nombre} - {self.conteo_detecciones} detecciones'
