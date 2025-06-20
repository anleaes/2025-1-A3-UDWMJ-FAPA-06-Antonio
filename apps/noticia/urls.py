from django.urls import path, include
from . import views

app_name = 'noticia'

urlpatterns = [
    path('adicionar/', views.add_noticia, name='add_noticia'),
    path('', views.list_noticia, name='list_noticia'),
    path('editar/<int:id_noticia>/', views.edit_noticia, name='edit_noticia'),
    path('excluir/<int:id_noticia>/', views.delete_noticia, name='delete_noticia'),
]