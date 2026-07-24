from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_edificios, name='lista_edificios'),
    path('edificios/<slug:slug>/', views.detalhe_edificio, name='detalhe_edificio'),
]