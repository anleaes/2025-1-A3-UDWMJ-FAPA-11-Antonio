from django.urls import path
from . import views

app_name = 'apps.categorias'

urlpatterns = [
    path('', views.listar_categorias, name='listar'),
    path('nova/', views.criar_categoria, name='criar'),
    path('editar/<int:id_categoria>/', views.editar_categoria, name='editar'),
    path('excluir/<int:id_categoria>/', views.excluir_categoria, name='excluir'),
]
