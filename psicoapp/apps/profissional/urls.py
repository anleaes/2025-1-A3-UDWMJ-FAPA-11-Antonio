from django.urls import path
from . import views

app_name= 'profissional'

urlpatterns = [
    path('', views.lista_profissional, name='list'),           
    path('novo/', views.adicionar_profissional, name='add'),       
    path('editar/<int:id>/', views.editar_profissional, name='edit'), 
    path('deletar/<int:id>/', views.deletar_profissional, name='delete'), 
]
