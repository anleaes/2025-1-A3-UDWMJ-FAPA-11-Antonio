from django.shortcuts import render, redirect, get_object_or_404
from .models import Prontuario
from .forms import ProntuarioForm

# Create your views here.

def listar_prontuarios(request):
    prontuarios = Prontuario.objects.all()
    return render(request, 'prontuarios/list.html', {'prontuarios': prontuarios})

def criar_prontuario(request):
    if request.method == 'POST':
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prontuarios:listar')
    else:
        form = ProntuarioForm()
    return render(request, 'prontuarios/form.html', {'form': form})

def editar_prontuario(request, id_prontuario):
    prontuario = get_object_or_404(Prontuario, id=id_prontuario)
    if request.method == 'POST':
        form = ProntuarioForm(request.POST, instance=prontuario)
        if form.is_valid():
            form.save()
            return redirect('prontuarios:listar')
    else:
        form = ProntuarioForm(instance=prontuario)
    return render(request, 'prontuarios/form.html', {'form': form})

def excluir_prontuario(request, id_prontuario):
    prontuario = get_object_or_404(Prontuario, id=id_prontuario)
    if request.method == 'POST':
        prontuario.delete()
        return redirect('prontuarios:listar')
    return render(request, 'prontuarios/confirm.html', {'prontuario': prontuario})
