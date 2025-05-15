from django.contrib import admin
from django.contrib.auth.models import User
from .models import Maquina, UserProfile, UserMachineAccess

# Personalizamos cómo se ve el modelo User en el admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')

# Primero quitamos el User anterior
admin.site.unregister(User)
# Y lo registramos de nuevo con nuestra personalización
admin.site.register(User, UserAdmin)

# Registramos Maquina
# @admin.register(Maquina)
# class MaquinaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombre')
#     search_fields = ('nombre',)

# Registramos UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username',)

# Registramos UserMachineAccess
@admin.register(UserMachineAccess)
class UserMachineAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'maquina', 'rango')
    list_filter = ('rango',)
    search_fields = ('profile__user__username', 'maquina__nombre')
