"""
URL configuration for victortools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views  # Importa la vista que creaste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # conecta el urls.py de core
    path('api/usuarios/', include('usuarios.urls')),
    path('', views.home),  # Aquí rediriges la raíz a una vista, como home
]
