from django.shortcuts import render, redirect, get_object_or_404
from .forms import FonteForm
from .models import Fonte


# Create your views here.

def add_fonte(request):
    template_name = 'fonte/add_fonte.html'
    context = {}
    if request.method == 'POST':
        form = FonteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = FonteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_fonte(request):
    template_name = 'fonte/list_fonte.html'
    fonte = Fonte.objects.filter()
    context = {
        'fonte': fonte
    }
    return render(request, template_name, context)

def edit_fonte(request, id_fonte):
    template_name = 'fonte/add_fonte.html'
    context ={}
    fonte = get_object_or_404(Fonte, id=id_fonte)
    if request.method == 'POST':
        form = FonteForm(request.POST, instance=fonte)
        if form.is_valid():
            form.save()
            return redirect('fonte:list_fonte')
    form = FonteForm(instance=fonte)
    context['form'] = form
    return render(request, template_name, context)

def delete_fonte(request, id_fonte):
    fonte = Fonte.objects.get(id=id_fonte)
    fonte.delete()
    return redirect('fonte:list_fonte')