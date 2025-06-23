from django.shortcuts import render
from ndia.models import Ndia, ItemNdia

# Create your views here.

def home(request):
    ndia = Ndia.objects.all()
    ndia_items = ItemNdia.objects.all()
    context = {
        'ndia': ndia,
        'ndia_items': ndia_items,
    }
    return render(request, 'core/home.html', context)