from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicamentoItem
from .forms import MedicamentoItemForm

# Create your views here.

def listar_medicamentoitens(request):
    itens = MedicamentoItem.objects.all()
    return render(request, 'medicamentoitens/list.html', {'itens': itens})

def criar_medicamentoitem(request):
    if request.method == 'POST':
        form = MedicamentoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamentoitens:listar')
    else:
        form = MedicamentoItemForm()
    return render(request, 'medicamentoitens/form.html', {'form': form, 'titulo': 'Cadastrar Item de Medicamento'})

def editar_medicamentoitem(request, id_item):
    item = get_object_or_404(MedicamentoItem, id=id_item)
    if request.method == 'POST':
        form = MedicamentoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('medicamentoitens:listar')
    else:
        form = MedicamentoItemForm(instance=item)
    return render(request, 'medicamentoitens/form.html', {'form': form, 'titulo': 'Editar Item de Medicamento'})

def excluir_medicamentoitem(request, id_item):
    item = get_object_or_404(MedicamentoItem, id=id_item)
    if request.method == 'POST':
        item.delete()
        return redirect('medicamentoitens:listar')
    return render(request, 'medicamentoitens/confirm.html', {'item': item})