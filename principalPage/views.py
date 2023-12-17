from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from interfaceAdmin.models import Envio

def home(request):
    return render(request,'principalPage/index/index.html')

@login_required
def seccion_cliente(request):
    return render(request, 'cliente/seccion_cliente.html')

def envioCliente(request):
    id_envio = request.GET.get('id_envio')
    envio = None
    if id_envio:
        try:
            envio = Envio.objects.select_related('id_estadoenvio').get(id_envio=id_envio)
        except Envio.DoesNotExist:
             messages.error(request, 'El envío con el ID proporcionado no existe.')
    return render(request, 'cliente/clienteListadoEnvios.html', {'envio': envio})
