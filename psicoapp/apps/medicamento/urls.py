from django.urls import path
from . import views

app_name = 'medicamentos'

urlpatterns = [
    path('', views.listar_medicamentos, name='listar'),
    path('criar/', views.criar_medicamento, name='criar'),
    path('editar/<int:id_medicamento>/', views.editar_medicamento, name='editar'),
    path('excluir/<int:id_medicamento>/', views.excluir_medicamento, name='excluir'),
]