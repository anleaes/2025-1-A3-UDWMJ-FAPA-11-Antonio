from django.urls import path
from . import views

app_name = 'prescricoes'

urlpatterns = [
    path('', views.listar_prescricoes, name='listar'),
    path('novo/', views.criar_prescricao, name='criar'),
    path('editar/<int:id_prescricao>/', views.editar_prescricao, name='editar'),
    path('excluir/<int:id_prescricao>/', views.excluir_prescricao, name='excluir'),
]
