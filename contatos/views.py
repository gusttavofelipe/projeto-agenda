from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def detalhes(request, contato_id): 
    detalhes = Contato.objects.get(id=contato_id) # id recebido como paramentro no link do index
    return render(request, 'contatos/detalhes.html', { # pagina de detalhes dos contatos
        'detalhe': detalhes
    })
