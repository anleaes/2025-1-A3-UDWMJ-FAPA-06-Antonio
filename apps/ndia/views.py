from django.shortcuts import render, redirect, get_object_or_404

from .forms import NdiaForm, ItemNdiaForm
from .models import Ndia , ItemNdia, Noticia, Editor


def add_ndia(request, id_editor):
    template_name = 'ndia/add_ndia.html'
    context = {}
    if request.method == 'POST':
        form = NdiaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.editor = Editor.objects.get(id=id_editor)
            f.save()
            form.save_m2m()
            return redirect('ndia:list_ndia')
    form = NdiaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_ndia(request):
    template_name = 'ndia/list_ndia.html'
    ndia = Ndia.objects.filter()
    ndia_items = ItemNdia.objects.filter()
    noticia = Noticia.objects.filter()
    editor = Editor.objects.filter()
    context = {
        'ndia': ndia,
        'ndia_items': ndia_items,
        'noticia': noticia,
        'editor': editor
    }
    return render(request, template_name, context)

def delete_ndia(request, id_ndia):
    ndia = Ndia.objects.get(id=id_ndia)
    ndia.delete()
    return redirect('ndia:list_ndia')

def add_ndia_item(request, id_ndia):
    template_name = 'ndia/add_ndia_item.html'
    context = {}
    if request.method == 'POST':
        form = ItemNdiaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ndia = Ndia.objects.get(id=id_ndia)
            f.save()
            form.save_m2m()
            return redirect('ndia:list_ndia')
    form = ItemNdiaForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_ndia_item(request, id_ndia_item):
    ndiaitem = ItemNdia.objects.get(id=id_ndia_item)
    ndiaitem.delete()
    return redirect('ndia:list_ndia')

