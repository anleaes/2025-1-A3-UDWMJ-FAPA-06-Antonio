from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm
from .models import Autor


# Create your views here.

def add_autor(request):
    template_name = 'autor/add_autor.html'
    context = {}
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = AutorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_autor(request):
    template_name = 'autor/list_autor.html'
    autor = Autor.objects.filter()
    context = {
        'autor': autor
    }
    return render(request, template_name, context)

def edit_autor(request, id_autor):
    template_name = 'autor/add_autor.html'
    context ={}
    autor = get_object_or_404(Autor, id=id_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor:list_autor')
    form = AutorForm(instance=autor)
    context['form'] = form
    return render(request, template_name, context)

def delete_autor(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    autor.delete()
    return redirect('autor:list_autor')