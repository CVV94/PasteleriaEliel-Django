from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from interfaceAdmin.models import Producto, PresentacionProducto, Valor
from interfaceAdmin.forms import *

def home(request):
    return render(request,'principalPage/index/index.html')

@login_required
def seccion_cliente(request):
    return render(request, 'cliente/seccion_cliente.html')

def homeCliente(request):
    return render(request, 'interfaceCliente/index.html')


