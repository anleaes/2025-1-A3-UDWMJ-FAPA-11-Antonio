from django.shortcuts import render, redirect, get_object_or_404
from .models import Atendimento
from .forms import AtendimentoForm

def listar_atendimentos(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'atendimentos/list.html', {'atendimentos': atendimentos})

def criar_atendimento(request):
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('atendimentos:listar')
    return render(request, 'atendimentos/form.html', {'form': form, 'titulo': 'Novo Atendimento'})

def editar_atendimento(request, id_atendimento):
    atendimento = get_object_or_404(Atendimento, id=id_atendimento)
    form = AtendimentoForm(request.POST or None, instance=atendimento)
    if form.is_valid():
        form.save()
        return redirect('atendimentos:listar')
    return render(request, 'atendimentos/form.html', {'form': form, 'titulo': 'Editar Atendimento'})

def deletar_atendimento(request, id_atendimento):
    atendimento = get_object_or_404(Atendimento, id=id_atendimento)
    if request.method == 'POST':
        atendimento.delete()
        return redirect('atendimentos:listar')
    return render(request, 'atendimentos/confirm_delete.html', {'obj': atendimento})
