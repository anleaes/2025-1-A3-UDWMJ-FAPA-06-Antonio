from django.urls import path, include
from . import views

app_name = 'autor'

urlpatterns = [
    path('adicionar/', views.add_autor, name='add_autor'),
    path('', views.list_autor, name='list_autor'),
    path('editar/<int:id_autor>/', views.edit_autor, name='edit_autor'),
    path('excluir/<int:id_autor>/', views.delete_autor, name='delete_autor'),
]