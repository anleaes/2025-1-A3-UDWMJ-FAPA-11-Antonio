"""
URL configuration for psicoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('especialidades/', include('especialidades.urls', namespace='especialidades')),
    path('profissionais/', include('apps.profissionais.urls', namespace='profissionais')),
    path('pacientes/', include('apps.pacientes.urls', namespace='pacientes')),
    path('atendimentos/', include('apps.atendimentos.urls', namespace='atendimentos')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('medicamentos/', include('apps.medicamentos.urls', namespace='medicamentos')),
    path('prescricoes/', include('apps.prescricoes.urls', namespace='prescricoes')),
    path('prontuarios/', include('apps.prontuarios.urls', namespace='prontuarios')),
    path('medicamentoitens/', include('apps.medicamentoitens.urls', namespace='medicamentoitens')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
