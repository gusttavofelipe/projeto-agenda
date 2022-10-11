import email
from django.contrib import admin
from .models import Categoria, Contato # importando models

class ContadoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar' ) # exibindo informações em contato
    list_display_links = ('id', 'nome',) # adiciona um link no campo desejado
    list_filter = ('nome', 'sobrenome', ) # adiciona um filtro com os campos desejados
    list_per_page = 10 # define quantos elemetos por tabela serão exbidos por pagina
    search_fields = ('id', 'nome', 'sobrenome') # adiciona à area de pesquisa os campos desejados
    list_editable = ('telefone', 'mostrar') # tornando campos listados editaveis/interativos

class CategoriaAdmin(admin.ModelAdmin):
   pass


admin.site.register(Categoria, CategoriaAdmin) # inserindo model na area adminstrativa
admin.site.register(Contato, ContadoAdmin) # inserindo model na area adminstrativa
