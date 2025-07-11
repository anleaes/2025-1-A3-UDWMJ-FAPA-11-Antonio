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

def editar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id=id_paciente)
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pacientes:listar')

    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Editar Paciente'})


def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes:listar')
    return render(request, 'pacientes/confirm_delete.html', {'paciente': paciente})
