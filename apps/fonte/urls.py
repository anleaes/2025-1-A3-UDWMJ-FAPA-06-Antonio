from django.urls import path, include
from . import views

app_name = 'fonte'

urlpatterns = [
    path('adicionar/', views.add_fonte, name='add_fonte'),
    path('', views.list_fonte, name='list_fonte'),
    path('editar/<int:id_fonte>/', views.edit_fonte, name='edit_fonte'),
    path('excluir/<int:id_fonte>/', views.delete_fonte, name='delete_fonte'),
]