from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('aguardando-aprovacao/', views.aguardando_aprovacao, name='aguardando_aprovacao'),
]