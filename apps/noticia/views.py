from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticiaForm
from .models import Noticia, NoticiaCategoria


# Create your views here.

def add_noticia(request):
    template_name = 'noticia/add_noticia.html'
    context = {}
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = NoticiaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_noticia(request):
    template_name = 'noticia/list_noticia.html'
    noticias = Noticia.objects.all()
    noticiascategorias = NoticiaCategoria.objects.all()
    context = {
        'noticia': noticias,
        'noticiascategorias': noticiascategorias,
    }
    return render(request, template_name, context)

def edit_noticia(request, id_noticia):
    template_name = 'noticia/add_noticia.html'
    context ={}
    noticia = get_object_or_404(Noticia, id=id_noticia)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticia:list_noticia')
    form = NoticiaForm(instance=noticia)
    context['form'] = form
    return render(request, template_name, context)

def delete_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)
    noticia.delete()
    return redirect('noticia:list_noticia')