from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models import Q, Value
from contatos.models import Contato
from django.http import Http404

def index(request):            # ordenando por id decrescente
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True # filtrando pela variavel quando for verdadeira
    )
    paginador = Paginator(contatos, 7) # numero de contatos por pagina

    num_paginas = request.GET.get('p') # variavel que contem numeração das paginas
    contatos = paginador.get_page(num_paginas)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
                                       

def detalhes(request, contato_id): 
    detalhes = get_object_or_404(Contato, id=contato_id) # levantando erro 404

    if not detalhes.mostrar: 
        raise Http404

    return render(request, 'contatos/detalhes.html', { 
        'detalhe': detalhes
    })


def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome') # Value simula um campo no db

    if termo is None:
        raise Http404() 

    contatos = Contato.objects.annotate(
        nome_completo=campos).filter(
            Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )       # pesquisando parcialmente nome e sobrenome e telefone

    # print(contatos.query)
    paginador = Paginator(contatos, 7) # numero de contatos por pagina

    num_paginas = request.GET.get('p') # variavel que contem numeração das paginas
    contatos = paginador.get_page(num_paginas)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })