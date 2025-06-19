from django import forms
from .models import Fonte

class FonteForm(forms.ModelForm):

    class Meta:
        model = Fonte
        exclude = ()