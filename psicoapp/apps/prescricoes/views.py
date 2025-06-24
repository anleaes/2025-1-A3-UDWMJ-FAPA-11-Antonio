from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescricao
from .forms import PrescricaoForm

# Create your views here.

def listar_prescricoes(request):
    prescricoes = Prescricao.objects.all()
    return render(request, 'prescricoes/listar.html', {'prescricoes': prescricoes})

def criar_prescricao(request):
    if request.method == 'POST':
        form = PrescricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescricoes:listar')
    else:
        form = PrescricaoForm()
    return render(request, 'prescricoes/form.html', {'form': form})

def editar_prescricao(request, id_prescricao):
    prescricao = get_object_or_404(Prescricao, id=id_prescricao)
    if request.method == 'POST':
        form = PrescricaoForm(request.POST, instance=prescricao)
        if form.is_valid():
            form.save()
            return redirect('prescricoes:listar')
    else:
        form = PrescricaoForm(instance=prescricao)
    return render(request, 'prescricoes/form.html', {'form': form})

def excluir_prescricao(request, id_prescricao):
    prescricao = get_object_or_404(Prescricao, id=id_prescricao)
    if request.method == 'POST':
        prescricao.delete()
        return redirect('prescricoes:listar')
    return render(request, 'prescricoes/confirmar_exclusao.html', {'prescricao': prescricao})
