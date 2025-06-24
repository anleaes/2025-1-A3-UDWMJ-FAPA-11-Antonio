from django.urls import path
from . import views

app_name = 'atendimentos'

urlpatterns = [
    path('', views.listar_atendimentos, name='listar'),
    path('novo/', views.criar_atendimento, name='criar'),
    path('editar/<int:id_atendimento>/', views.editar_atendimento, name='editar'),
    path('excluir/<int:id_atendimento>/', views.excluir_atendimento, name='excluir'),  
]