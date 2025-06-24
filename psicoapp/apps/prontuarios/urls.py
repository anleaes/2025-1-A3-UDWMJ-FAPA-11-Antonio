from django.urls import path
from . import views

app_name = 'prontuarios'

urlpatterns = [
    path('', views.listar_prontuarios, name='listar'),
    path('novo/', views.criar_prontuario, name='criar'),
    path('editar/<int:id_prontuario>/', views.editar_prontuario, name='editar'),
    path('excluir/<int:id_prontuario>/', views.excluir_prontuario, name='excluir'),
]
