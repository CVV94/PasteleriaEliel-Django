from django.shortcuts import render,redirect
from .forms import ProductoForm,CargarImagenForm,ValorForm
from .models import Producto
from django.db.models import F

# Create your views here.
def interfaceAdmin(request):
    return render(request,'interfaceAdmin/interfaceHome/interfazAdmin.html')


def registrarProducto(request):
    form_producto = ProductoForm()
    mensaje = {}

    if request.method == 'POST':
        nombreSelect = request.POST.get('nombre')
        form_producto = ProductoForm(request.POST)
        nombreProducto = Producto.objects.filter(nombre=nombreSelect)
        
        if nombreProducto:
            mensaje['mensajeProducto'] = 'El Producto (' + str(nombreSelect) + ') ya existe'
        elif form_producto.is_valid():
            form_producto.save()
            mensaje['mensajeProducto'] = 'El Producto (' + str(nombreSelect) + ') se guardó correctamente'

    return render(request,'interfaceAdmin/adminFormularios/registrarProductos.html',{'form_producto':form_producto})

def registrarValor(request):
    form_valor = ValorForm()
    mensaje = {}

    if request.method == 'POST':
        form_valor = ValorForm(request.POST)
        if form_valor.is_valid():
            form_valor.save()
            mensaje['mensajeValor'] = 'El Valor se registró correctamente'

    return render(request,'interfaceAdmin/adminFormularios/registrarPrecio.html',{'form_valor':form_valor})


def registrarImagen(request):
    form_imagen = CargarImagenForm()
    mensaje = {}

    if request.method == 'POST':
        form_imagen = CargarImagenForm(request.POST, request.FILES)
        if form_imagen.is_valid():
            form_imagen.save()
            mensaje['mensajeImagen'] = 'La Imagen se registró correctamente'

    return render(request,'interfaceAdmin/adminFormularios/registrarImagen.html',{'form_imagen':form_imagen})




def listadoProductos(request):
    productos = Producto.objects.filter(estado='ACTIVO').values(
        'id_producto', 'nombre', 'tipo', 'descripcion'
    ).annotate(
        stock=F('valor__stock'), 
        imagen=F('presentacionproducto__imagen'), 
        precio=F('valor__precio')
    )

    return render(request, 'interfaceAdmin/adminFormularios/listadoProductos.html', {'productos': productos})




def editarProductos(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('listadoProducto')
    return render(request,'item22App/editarProducto.html',{'form':form})

def eliminarProductos(request,id_producto):
    producto= Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect('listadoProducto')