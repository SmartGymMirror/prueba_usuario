from django.urls import path
from .views import registro, inicio_sesion

urlpatterns = [
    path('api/registro/', registro, name='registro'),
    path('api/inicio_sesion/', inicio_sesion, name='inicio_sesion'),
]