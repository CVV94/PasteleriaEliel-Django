from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login ,authenticate,login,logout
from django.contrib.auth.models import Group,User



def registro_cliente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            # Asignar al grupo de clientes
            grupo_cliente, creado = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo_cliente)
            user = authenticate(request, username=username, password=password1)
            auth_login(request, user)  # Iniciar sesión automáticamente después del registro
            # Redirigir a la página de inicio o a una sección específica para clientes
            return redirect('home')
        else:
            # Las contraseñas no coinciden, maneja el error aquí
            mensaje='Las contraseñas no coinciden'
            return render(request, 'Register/cliente/registro_cliente.html', {'mensaje':mensaje})
    return render(request, 'Register/cliente/registro_cliente.html')

def login_cliente(request):
    form = AuthenticationForm(request, data=(request.POST if request.method == 'POST' else None))
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid username or password.")
        elif user.is_superuser:
            login(request, user)
            return redirect('interfazAdministrador')
        elif user.groups.filter(name='Clientes').exists():
            login(request, user)
            return redirect('seccion_cliente')

    return render(request, 'Register/cliente/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio o a donde prefieras después de cerrar sesión
    return redirect('home')