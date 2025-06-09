from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfissionalForm
from .models import Profissional, ProfissionalEspecialidade
from especialidades.models import Especialidade

def lista_profissional(request):
    profissionais = Profissional.objects.all()
    especialidades = ProfissionalEspecialidade.objects.select_related('especialidade', 'profissional')
    return render(request, 'profissional/list.html', {
        'profissionais': profissionais,
        'especialidades': especialidades
    })

def adicionar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            profissional = form.save()
            especialidade = form.cleaned_data['especialidade']
            registro = form.cleaned_data['registro_conselho']
            ProfissionalEspecialidade.objects.create(
                profissional=profissional,
                especialidade=especialidade,
                registro_conselho=registro
            )
            return redirect('profissional:list')
    else:
        form = ProfissionalForm()
    return render(request, 'profissional/form.html', {'form': form})

def editar_profissional(request, id):
    profissional = get_object_or_404(Profissional, pk=id)
    especialidade_relacionada = ProfissionalEspecialidade.objects.filter(profissional=profissional).first()
    
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            profissional = form.save()
            especialidade = form.cleaned_data['especialidade']
            registro = form.cleaned_data['registro_conselho']

            if especialidade_relacionada:
                especialidade_relacionada.especialidade = especialidade
                especialidade_relacionada.registro_conselho = registro
                especialidade_relacionada.save()
            else:
                ProfissionalEspecialidade.objects.create(
                    profissional=profissional,
                    especialidade=especialidade,
                    registro_conselho=registro
                )

            return redirect('profissional:list')
    else:
        dados_iniciais = {
            'especialidade': especialidade_relacionada.especialidade if especialidade_relacionada else None,
            'registro_conselho': especialidade_relacionada.registro_conselho if especialidade_relacionada else '',
        }
        form = ProfissionalForm(instance=profissional, initial=dados_iniciais)
    
    return render(request, 'profissional/form.html', {'form': form})

def deletar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)
    if request.method == 'POST':
        profissional.delete()
        return redirect('profissional:list')
    return render(request, 'profissional/confirm_delete.html', {'profissional': profissional})

def home(request):
    return render(request, 'home.html')
