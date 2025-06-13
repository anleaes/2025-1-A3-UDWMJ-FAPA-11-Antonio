from django.shortcuts import render, redirect, get_object_or_404
from .models import Profissional
from .forms import ProfissionalForm

def listar_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'profissionais/list.html', {'profissionais': profissionais})

def criar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profissionais:listar')
    else:
        form = ProfissionalForm()
    return render(request, 'profissionais/form.html', {'form': form})

def editar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('profissionais:list')
    else:
        form = ProfissionalForm(instance=profissional)
    return render(request, 'profissionais/form.html', {'form': form})

def excluir_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)
    profissional.delete()
    return redirect('profissionais:list')

