from xml.etree.ElementInclude import default_loader
from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str: # representando objetos pelo nome(no site)
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255) # adicionando campo nome
    sobrenome = models.CharField(max_length=255, blank=True) # adicionando campo sobrenome
    telefone = models.CharField(max_length=255) # adicionando campo telefone
    email = models.CharField(max_length=255, blank=True) # adicionando campo email
    data_criacao = models.DateTimeField(default=timezone.now) # adicionando campo data da criação
    descricao =models.TextField(blank=True) # adicionando campo descrição
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) # adicionando categoria a ser selecionada
    mostrar = models.BooleanField(default=True) # campo de alteraração de visualização de um contato

    def __str__(self) -> str: # representando objetos pelo nome(no site)
        return self.nome