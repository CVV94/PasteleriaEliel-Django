from django.shortcuts import render,redirect
from .forms import ProductoForm,CargarImagenForm,ValorForm, ProveedorForm, IngredienteForm, EnvioForm, CompraForm
from .models import Producto, Proveedor, Ingrediente, Compra, Envio, Estadoenvio, Cliente, CarritoCompra, Estadopago
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



# PROVEEDORES
def listadoProveedores(request):
    proveedores = Proveedor.objects.all()
    data = {'proveedores':proveedores}
    return render(request,'interfaceAdmin/adminFormularios/listadoProveedores.html', data)

def registrarProveedor(request):
    form_proveedor = ProveedorForm()
    mensaje = {}

    if request.method == 'POST':
        nombreSelect = request.POST.get('nombre')
        form_proveedor = ProveedorForm(request.POST)
        nombreProveedor = Proveedor.objects.filter(nombre=nombreSelect)
        
        if nombreProveedor:
            mensaje['mensajeProveedor'] = 'El Proveedor (' + str(nombreSelect) + ') ya existe'
        elif form_proveedor.is_valid():
            form_proveedor.save()
            mensaje['mensajeProveedor'] = 'El Proveedor (' + str(nombreSelect) + ') se guardó correctamente'

    return render(request,'interfaceAdmin/adminFormularios/registrarProveedor.html',{'form_proveedor':form_proveedor})


def editarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    form = ProveedorForm(instance=proveedor)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
        return redirect('listadoProveedores')
    return render(request,'interfaceAdmin/adminFormularios/registrarProveedor.html',{'form':form})

def eliminarProveedor(request,id_proveedor):
    proveedor= Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect('listadoProveedores')





# INGREDIENTES
def listadoIngredientes(request):
    ingredientes = Ingrediente.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    data = {
        'ingredientes':ingredientes,
        'productos':productos,
        'proveedores':proveedores
        }
    return render(request,'interfaceAdmin/adminFormularios/listadoIngredientes.html', data)

def registrarIngrediente(request):
    form = IngredienteForm()
    if request.method == 'POST' :
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listadoIngredientes')
    data = {'form':form, 'titulo' : 'AGREGAR INGREDIENTE'}
    return render(request, 'interfaceAdmin/adminFormularios/registrarIngrediente.html', data)

def editarIngrediente(request,id_ingrediente):
    ingrediente=Ingrediente.objects.get(id_ingrediente=id_ingrediente)
    form = IngredienteForm(instance=ingrediente)
    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
        return redirect('listadoIngredientes')
    
    data = {'form' : form, 'titulo' : 'ACTUALIZAR INGREDIENTE'}
    return render(request,'interfaceAdmin/adminFormularios/registrarIngrediente.html',data)

def eliminarIngrediente(request,id_ingrediente):
    ingrediente= Ingrediente.objects.get(id_ingrediente=id_ingrediente)
    ingrediente.delete()
    return redirect('interfaceAdmin/adminFormularios/listadoIngredientes.html')



# ENVIOS
def listadoEnvios(request):
    envios = Envio.objects.all()
    compras = Compra.objects.all()
    estadoenvios = Estadoenvio.objects.all()
    data = {
        'envios':envios,
        'compras':compras,
        'estadoenvios':estadoenvios
        }
    return render(request,'interfaceAdmin/adminFormularios/listadoEnvios.html', data)

def registrarEnvio(request):
    form = EnvioForm()
    if request.method == 'POST' :
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listadoEnvios')
    data = {'form':form, 'titulo' : 'AGREGAR ENVIO'}
    return render(request, 'interfaceAdmin/adminFormularios/registrarEnvio.html', data)

def editarEnvio(request,id_envio):
    envio=Envio.objects.get(id_envio=id_envio)
    form = EnvioForm(instance=envio)
    if request.method == 'POST':
        form = EnvioForm(request.POST, instance=envio)
        if form.is_valid():
            form.save()
        return redirect('listadoEnvios')
    
    data = {'form' : form, 'titulo' : 'ACTUALIZAR ENVIO'}
    return render(request,'interfaceAdmin/adminFormularios/registrarEnvio.html',data)

def eliminarEnvio(request,id_envio):
    envio= Ingrediente.objects.get(id_envio=id_envio)
    envio.delete()
    return redirect('interfaceAdmin/adminFormularios/listadoEnvios.html')




# COMPRAS
def listadoCompras(request):
    compras = Compra.objects.all()
    clientes = Cliente.objects.all()
    carritos = CarritoCompra.objects.all()
    estadoPagos = Estadopago.objects.all()
    data = {
        'compras':compras,
        'clientes':clientes,
        'carritos':carritos,
        'estadoPagos':estadoPagos
        }
    return render(request,'interfaceAdmin/adminFormularios/listadoCompras.html', data)

def registrarCompra(request):
    form = CompraForm()
    if request.method == 'POST' :
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listadoCompras')
    data = {'form':form, 'titulo' : 'AGREGAR COMPRA'}
    return render(request, 'interfaceAdmin/adminFormularios/registrarCompra.html', data)

def editarCompra(request,id_compra):
    compra=Compra.objects.get(id_compra=id_compra)
    form = CompraForm(instance=compra)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
        return redirect('listadoCompras')
    
    data = {'form' : form, 'titulo' : 'ACTUALIZAR COMPRA'}
    return render(request,'interfaceAdmin/adminFormularios/registrarConpra.html',data)

def eliminarCompra(request,id_compra):
    compra= Compra.objects.get(id_compra=id_compra)
    compra.delete()
    return redirect('interfaceAdmin/adminFormularios/listadoCompras.html')



def listadoProductosCarta(request):
    productos = Producto.objects.all()
    return render(request, 'interfaceCliente/carta.html', {'productos': productos})


def homeCliente(request):
    return render(request, 'interfaceCliente/index.html')

def homeProductos(request):
    return render(request, 'interfaceCliente/inicioCliente.html')

def carta(request):
    return render(request, 'interfaceCliente/carta.html')