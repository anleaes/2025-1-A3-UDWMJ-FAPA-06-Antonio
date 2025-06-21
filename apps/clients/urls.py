from django.urls import path, include
from . import views

app_name = 'clients'

urlpatterns = [
    path('adicionar/', views.add_clients, name='add_clients'),
    path('', views.list_clients, name='list_clients'),
    path('editar/<int:id_clients>/', views.edit_clients, name='edit_clients'),
    path('excluir/<int:id_clients>/', views.delete_clients, name='delete_clients'),
]