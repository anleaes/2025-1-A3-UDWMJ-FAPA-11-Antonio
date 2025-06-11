from django.urls import path
from . import views

app_name = 'profissionais'

urlpatterns = [
    path('', views.listar_profissionais, name='list'),
    path('criar/', views.criar_profissional, name='criar'),
    path('editar/<int:id>/', views.editar_profissional, name='edit'),
    path('excluir/<int:id>/', views.excluir_profissional, name='delete'), 
]
