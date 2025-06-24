from django.shortcuts import render, redirect, get_object_or_404
from .forms import EspecialidadeForm
from .models import Especialidade
from django.shortcuts import get_object_or_404

def list_especialidades(request):
    template_name = 'especialidades/list.html'
    especialidades = Especialidade.objects.all()
    context = {'especialidades': especialidades}
    return render(request, template_name, context)

def add_especialidade(request):
    template_name = 'especialidades/add.html'
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especialidades:list')
    else:
        form = EspecialidadeForm()
    return render(request, template_name, {'form': form})

def edit_especialidade(request, id_especialidade):
    template_name = 'especialidades/add.html'
    especialidade = get_object_or_404(Especialidade, id=id_especialidade)
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('especialidades:list')
    else:
        form = EspecialidadeForm(instance=especialidade)
    return render(request, template_name, {'form': form})

def delete_especialidade(request, id_especialidade):
    especialidade = get_object_or_404(Especialidade, id=id_especialidade)
    especialidade.delete()
    return redirect('especialidades:list')

def home(request):
    return render(request, 'home.html')
