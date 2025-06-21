from django.urls import path, include
from . import views

app_name = 'editor'

urlpatterns = [
    path('adicionar/', views.add_editor, name='add_editor'),
    path('', views.list_editor, name='list_editor'),
    path('editar/<int:id_editor>/', views.edit_editor, name='edit_editor'),
    path('excluir/<int:id_editor>/', views.delete_editor, name='delete_editor'),
]