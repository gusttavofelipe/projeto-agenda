from django.db import models
from contatos.models import Contato
from django import forms

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato # formulario importado 
        exclude = ('mostrar',) # exclue campos do form