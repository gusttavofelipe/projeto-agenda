from django.shortcuts import render, get_object_or_404
from contatos.models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def detalhes(request, contato_id): 
    detalhes = get_object_or_404(Contato, id=contato_id) # levantando erro 404
    return render(request, 'contatos/detalhes.html', { 
        'detalhe': detalhes
    })
