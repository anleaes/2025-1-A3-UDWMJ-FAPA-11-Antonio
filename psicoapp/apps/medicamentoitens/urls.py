from django.urls import path
from . import views

app_name = 'medicamentoitens'

urlpatterns = [
    path('', views.listar_medicamentoitens, name='listar'),
    path('criar/', views.criar_medicamentoitem, name='criar'),
    path('editar/<int:id_item>/', views.editar_medicamentoitem, name='editar'),
    path('excluir/<int:id_item>/', views.excluir_medicamentoitem, name='excluir'),
]