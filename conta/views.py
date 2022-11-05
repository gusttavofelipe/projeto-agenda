from django.shortcuts import render

def login(request):
    return render(request, 'conta/login.html')

def logout(request):
    return render(request, 'conta/logout.html')

def cadastro(request):
    return render(request, 'conta/cadastro.html')

def dashboard(request):
    return render(request, 'conta/dashboard.html')
