from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditorForm
from .models import Editor


# Create your views here.

def add_editor(request):
    template_name = 'editor/add_editor.html'
    context = {}
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = EditorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_editor(request):
    template_name = 'editor/list_editor.html'
    editor = Editor.objects.filter()
    context = {
        'editor': editor
    }
    return render(request, template_name, context)

def edit_editor(request, id_editor):
    template_name = 'editor/add_editor.html'
    context ={}
    editor = get_object_or_404(Editor, id=id_editor)
    if request.method == 'POST':
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
            return redirect('editor:list_editor')
    form = EditorForm(instance=editor)
    context['form'] = form
    return render(request, template_name, context)

def delete_editor(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    editor.delete()
    return redirect('editor:list_editor')