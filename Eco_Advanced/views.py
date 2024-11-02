from django.shortcuts import render

from django.shortcuts import render
from .models import Servico
def home(request):
    return render(request, 'eco_advanced/home.html')

def servicos(request):
    servicos_list = Servico.objects.all()
    return render(request, 'eco_advanced/servicos.html', {'servicos': servicos_list})

def contato(request):
    return render(request, 'eco_advanced/contato.html')

def sobre(request):
    return render(request, 'eco_advanced/sobre.html')
