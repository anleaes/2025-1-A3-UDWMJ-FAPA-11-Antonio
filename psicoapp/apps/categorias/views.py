from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/list.html', {'categorias': categorias})

def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorias:listar')
    return render(request, 'categorias/form.html', {'form': form, 'titulo': 'Nova Categoria'})

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('categorias:listar')
    return render(request, 'categorias/form.html', {'form': form, 'titulo': 'Editar Categoria'})

def excluir_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias:listar')
    return render(request, 'categorias/confirm.html', {'categoria': categoria})
