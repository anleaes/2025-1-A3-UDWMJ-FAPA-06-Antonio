from django import forms
from .models import Ndia, Editor, ItemNdia ,Noticia

class NdiaForm(forms.ModelForm):

    class Meta:
        model = Ndia
        exclude = ('editor',)

class ItemNdiaForm(forms.ModelForm):

    class Meta:
        model = ItemNdia
        exclude = ('ndia',)
