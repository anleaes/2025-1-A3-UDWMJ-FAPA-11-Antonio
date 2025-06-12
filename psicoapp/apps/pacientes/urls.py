from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.listar_pacientes, name='listar'),
    path('novo/', views.criar_paciente, name='criar'),
   path('editar/<int:id_paciente>/', views.editar_paciente, name='editar'),
    path('excluir/<int:id_paciente>/', views.excluir_paciente, name='excluir'),
]
