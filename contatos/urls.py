from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.detalhes, name='detalhes') ,
     # mandando argumento nomeado e tipado para views
    path('busca/', views.busca, name='busca') 
]  
