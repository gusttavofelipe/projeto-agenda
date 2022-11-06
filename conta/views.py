from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email

def login(request):
    return render(request, 'conta/login.html')

def logout(request):
    return render(request, 'conta/logout.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'conta/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email \
        or not usuario or not senha or not senha2:
        messages.error(request, 'PREENCHA TODOS OS CAMPOS')
        return render(request, 'conta/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        return render(request, 'conta/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário deve ter no mínimo 6 caracteres')
        return render(request, 'conta/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha deve ter no mínimo 6 caracteres')
        return render(request, 'conta/cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'Senhas não coincidem')
        return render(request, 'conta/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Este usuário já está cadastrado')
        return render(request, 'conta/cadastro.html')        

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este e-mail já está cadastrado')
        return render(request, 'conta/cadastro.html')


    messages.success(request, 'Cadastrado com sucesso. Pronto para logar!')

    user = User.objects.create_user(
        username=usuario, email=email, password=senha,
         first_name=nome, last_name=sobrenome)

    user.save
    return redirect('login')

def dashboard(request):
    return render(request, 'conta/dashboard.html')


