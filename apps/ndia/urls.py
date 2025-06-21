from django.urls import path
from . import views

app_name = 'ndia'

urlpatterns = [
    path('', views.list_ndia, name='list_ndia'),
    path('adicionar/<int:id_editor>/', views.add_ndia, name='add_ndia'),
    path('excluir/<int:id_ndia>/', views.delete_ndia, name='delete_ndia'),
    path('excluir-item/<int:id_ndia_item>/', views.delete_ndia_item, name='delete_ndia_item'),
    path('adicionar-item/<int:id_ndia>/', views.add_ndia_item, name='add_ndia_item'),
]