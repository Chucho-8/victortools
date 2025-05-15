from django.db import models

# Create your models here.
from django.contrib.auth.models import User
#from django.db import models
from core.models import Maquina 



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    maquinas = models.ManyToManyField(Maquina, through='UserMachineAccess', blank=True)

    def __str__(self):
        return f"{self.user.username}"

class UserMachineAccess(models.Model):
    RANGO_CHOICES = [
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Solo lectura'),
    ]

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    rango = models.CharField(max_length=10, choices=RANGO_CHOICES, default='viewer')

    class Meta:
        unique_together = ('profile', 'maquina')  # evita duplicados

    def __str__(self):
        return f"{self.profile.user.username} - {self.maquina.nombre} ({self.rango})"