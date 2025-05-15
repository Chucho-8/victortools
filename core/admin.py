from django.contrib import admin
from .models import Maquina, Registro, ConteoProduccion, Piston, Motor, SensorPeso, SensorOptico, HistorialProduccion

# admin.site.register(Maquina)
# admin.site.register(Registro)
# admin.site.register(ConteoProduccion)
# admin.site.register(Piston)
# admin.site.register(Motor)
# admin.site.register(SensorPeso)
# admin.site.register(SensorOptico)

# --- Admin para Maquina ---
@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'estado', 'ultima_actualizacion', 'usuario')
    list_filter = ('tipo', 'estado', 'usuario',)  # Filtros: por tipo de máquina y estado (encendida/apagada)
    search_fields = ('nombre', 'usuario',)  # Búsqueda por nombre
    ordering = ('nombre',)


# --- Admin para Registro ---
@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'mensaje', 'fecha')
    list_filter = ('maquina', 'fecha')  # Filtros: máquina y fecha
    search_fields = ('mensaje', 'maquina__nombre')  # Búsqueda por mensaje o nombre de máquina
    date_hierarchy = 'fecha'  # Agrega navegación por fecha arriba
    ordering = ('-fecha',)


# --- Admin para ConteoProduccion ---
@admin.register(ConteoProduccion)
class ConteoProduccionAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'cantidad', 'fecha')
    list_filter = ('maquina', 'fecha')  # Filtros: máquina y fecha
    search_fields = ('maquina__nombre',)  # Búsqueda por nombre de máquina
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)


# --- Admin para Piston ---
@admin.register(Piston)
class PistonAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'nombre', 'conteo_activaciones')
    list_filter = ('maquina',)  # Filtro solo por máquina
    search_fields = ('nombre', 'maquina__nombre')  # Búsqueda por nombre de pistón o de máquina
    ordering = ('maquina', 'nombre')


# --- Admin para Motor ---
@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'nombre', 'encendido', 'ultima_actualizacion')
    list_filter = ('maquina', 'encendido')  # Filtros: máquina y estado del motor
    search_fields = ('nombre', 'maquina__nombre')  # Búsqueda por nombre del motor o de máquina
    ordering = ('maquina', 'nombre')


# --- Admin para SensorPeso ---
@admin.register(SensorPeso)
class SensorPesoAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'peso_objetivo', 'peso_actual', 'ultima_actualizacion')
    list_filter = ('maquina',)  # Filtro por máquina
    search_fields = ('maquina__nombre',)  # Búsqueda por nombre de máquina
    ordering = ('maquina',)


# --- Admin para SensorOptico ---
@admin.register(SensorOptico)
class SensorOpticoAdmin(admin.ModelAdmin):
    list


# Registrar el modelo HistorialProduccion
@admin.register(HistorialProduccion)
class HistorialProduccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'maquina', 'cantidad_producida', 'fecha_hora', 'evento')  # Qué columnas se ven en la tabla
    list_filter = ('maquina', 'fecha_hora')  # Filtros por máquina y fecha
    search_fields = ('maquina__nombre', 'evento')  # Buscar por nombre de máquina o tipo de evento