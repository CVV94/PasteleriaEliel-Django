from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login ,authenticate,login,logout
from django.contrib.auth.models import Group


def registro_cliente(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar al grupo de clientes
            grupo_cliente, creado = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo_cliente)
            auth_login(request, user)  # Iniciar sesión automáticamente después del registro
            # Redirigir a la página de inicio o a una sección específica para clientes
            return redirect('seccion_cliente')
    else:
        form = UserCreationForm()
    return render(request, 'Register/cliente/registro_cliente.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la sección de clientes
                return redirect('seccion_cliente')
    else:
        form = AuthenticationForm()
    return render(request, 'Register/cliente/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio o a donde prefieras después de cerrar sesión
    return redirect('home')