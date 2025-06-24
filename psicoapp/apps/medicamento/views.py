from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicamento
from .forms import MedicamentoForm 

def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/list.html', {'medicamentos': medicamentos})

def criar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamentos:listar')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamentos/form.html', {'form': form, 'titulo': 'Cadastrar Medicamento'})

def editar_medicamento(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, id=id_medicamento)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamentos:listar')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamentos/form.html', {'form': form, 'titulo': 'Editar Medicamento'})

def excluir_medicamento(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, id=id_medicamento)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamentos:listar')
    return render(request, 'medicamentos/confirmar_exclusao.html', {'medicamento': medicamento})
