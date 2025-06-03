from django.urls import path
from . import views

app_name = 'especialidades'

urlpatterns = [
    path('', views.list_especialidades, name='list'),
    path('adicionar/', views.add_especialidade, name='add'),
    path('editar/<int:id_especialidade>/', views.edit_especialidade, name='edit'),
    path('excluir/<int:id_especialidade>/', views.delete_especialidade, name='delete'),
]