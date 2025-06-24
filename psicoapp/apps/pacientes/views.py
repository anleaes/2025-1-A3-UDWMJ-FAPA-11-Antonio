from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/list.html', {'pacientes': pacientes})

def criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes:listar')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes:listar')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form})

def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes:listar')
    return render(request, 'pacientes/confirm_delete.html', {'paciente': paciente})
