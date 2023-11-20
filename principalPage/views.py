from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'principalPage/index/index.html')

@login_required
def seccion_cliente(request):
    return render(request, 'cliente/seccion_cliente.html')