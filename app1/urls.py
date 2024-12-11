from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('juegos', views.juegos, name='Juegos')
]