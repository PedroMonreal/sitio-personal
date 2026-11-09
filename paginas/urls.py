# paginas/urls.py
from django.urls import path

from .views import vista_inicio, VistaAcercaDe, vista_saludo

urlpatterns = [
    path("saludo/<str:nombre>/", vista_saludo, name="saludo"),
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),  # nuevo
    path("", vista_inicio, name="inicio"),  # nuevo
]
