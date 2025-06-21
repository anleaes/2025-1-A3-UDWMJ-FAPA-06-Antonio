from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientsForm
from .models import Clients


# Create your views here.

def add_clients(request):
    template_name = 'clients/add_clients.html'
    context = {}
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = ClientsForm()
    context['form'] = form
    return render(request, template_name, context)

def list_clients(request):
    template_name = 'clients/list_clients.html'
    clients = Clients.objects.filter()
    context = {
        'clients': clients
    }
    return render(request, template_name, context)

def edit_clients(request, id_clients):
    template_name = 'clients/add_clients.html'
    context ={}
    clients = get_object_or_404(Clients, id=id_clients)
    if request.method == 'POST':
        form = ClientsForm(request.POST, instance=clients)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clients')
    form = ClientsForm(instance=clients)
    context['form'] = form
    return render(request, template_name, context)

def delete_clients(request, id_clients):
    clients = Clients.objects.get(id=id_clients)
    clients.delete()
    return redirect('clients:list_clients')