from django.shortcuts import render,redirect
from .forms import ProductoForm,CargarImagenForm,ValorForm, ProveedorForm, IngredienteForm, EnvioForm, CompraForm, CalificacionForm, DetalleCarritoForm
from .models import Producto, Proveedor, Ingrediente, Compra, Envio, Estadoenvio, Cliente, CarritoCompra, Estadopago, PresentacionProducto, Valor, Calificacion, DetalleCarritoCompraProducto
from django.db.models import F
from django.contrib import messages
from django.shortcuts import get_object_or_404

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




# PROCESO DE COMPRA

def listadoProductosCarta(request):
    productos = Producto.objects.all()
    return render(request, 'interfaceCliente/carta.html', {'productos': productos})

def format_precio_clp(precio):
    return "{:,.0f}".format(precio).replace(",", ".")


def detalleProducto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    form_carrito = DetalleCarritoForm(request.POST or None)
    form_calificacion = CalificacionForm(request.POST or None)
    calificaciones = Calificacion.objects.filter(id_producto=id_producto)
    valor = Valor.objects.filter(id_producto=id_producto).first()

    if request.method == 'POST':
        if 'agregar_carrito' in request.POST and form_carrito.is_valid():
            id_cliente = request.user.id
            carrito, _ = CarritoCompra.objects.get_or_create(id_cliente=id_cliente)
            detalle, created = DetalleCarritoCompraProducto.objects.get_or_create(
                id_carrito=carrito,
                id_producto=producto,
                defaults={'cantidad': form_carrito.cleaned_data['cantidad'], 'precio_unitario': valor.precio}
            )
            if not created:
                detalle.cantidad += form_carrito.cleaned_data['cantidad']
                detalle.save()
            return redirect('detalleProducto', id_producto=id_producto)

        elif 'agregar_calificacion' in request.POST and form_calificacion.is_valid():
            nueva_calificacion = form_calificacion.save(commit=False)
            nueva_calificacion.id_producto = producto
            nueva_calificacion.save()
            return redirect('detalleProducto', id_producto=id_producto)

    precio_formato_clp = format_precio_clp(valor.precio) if valor else 'No Disponible'

    context = {
        'producto': producto,
        'form_carrito': form_carrito,
        'form_calificacion': form_calificacion,
        'calificaciones': calificaciones,
        'precio_formato_clp': precio_formato_clp
    }
    return render(request, 'interfaceCliente/productoDetalle.html', context)




def vista_del_carrito(request):
    # Obtener el carrito de la sesión
    carrito = request.session.get('carrito', {})

    # Recuperar información adicional de los productos y sus precios
    detalles_del_carrito = []
    for id_producto, cantidad in carrito.items():
        producto = Producto.objects.get(pk=id_producto)
        valor = Valor.objects.filter(id_producto=id_producto).first()
        subtotal = valor.precio * cantidad if valor else 0

        detalles_del_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    context = {
        'detalles_del_carrito': detalles_del_carrito,
        'total': sum(item['subtotal'] for item in detalles_del_carrito)
    }
    return render(request, 'interfaceCliente/descripcionCarrito.html', context)




def descripcionCarrito(request):
    id_cliente = request.user.id
    carrito = CarritoCompra.objects.get(id_cliente=id_cliente)
    detalles = carrito.detallecarritocompraproducto_set.all()

    context = {
        'detalles': detalles,
    }
    return render(request, 'descripcionCarrito.html', context)


def carta(request):
    return render(request, 'interfaceCliente/carta.html')