from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.listar_pacientes, name='listar'),
    path('novo/', views.criar_paciente, name='criar'),
    path('editar/<int:paciente_id>/', views.editar_paciente, name='editar'),
    path('excluir/<int:paciente_id>/', views.excluir_paciente, name='excluir'),
]
