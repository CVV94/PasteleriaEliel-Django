from pyexpat.errors import messages
from typing import Any
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import ProductoForm,CargarImagenForm,ValorForm, ProveedorForm, IngredienteForm, EnvioForm, CompraForm,EstadoEnvioForm, DetalleCarritoForm, CalificacionForm
from .models import Producto, Proveedor, Ingrediente, Compra, Envio, Estadoenvio, Cliente, CarritoCompra, Estadopago, PresentacionProducto,Valor, DetalleCarritoCompraProducto, Calificacion
from django.db.models import F
from django.urls import reverse_lazy
import os
from django.http import Http404
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def interfaceAdmin(request):
    return render(request,'interfaceAdmin/interfaceHome/interfazAdmin.html')

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'interfaceAdmin/adminFormularios/registrarProductos.html'
    form_class = ProductoForm
    success_url = reverse_lazy('listadoDeProductos') 
    context_object_name = 'productos'

    def form_valid(self, form):
        nombre_select = form.cleaned_data['nombre']
        nombre_producto = Producto.objects.filter(nombre=nombre_select)

        if nombre_producto:
            mensaje = f'El Producto ({nombre_select}) ya existe'
            return render(self.request, self.template_name, {'form': form, 'mensaje': mensaje})
        else:
            form.save()
            mensaje = f'El Producto ({nombre_select}) se ha registrado correctamente'
            return render(self.request, self.template_name, {'form': form, 'mensaje': mensaje})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Registrar Productos'
        return context    
    
class ValorCreateView(CreateView):
    model = Valor
    template_name = 'interfaceAdmin/adminFormularios/registrarPrecio.html'
    form_class = ValorForm
    success_url = reverse_lazy('registrarPrecio') 
    context_object_name = 'form'

    def form_valid(self, form):
        valor=form.save()
        mensaje = f'El Valor: {valor.precio} se ha registrado correctamente'
        return render(self.request, self.template_name, {'form': form, 'mensaje': mensaje})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Registrar Productos'
        return context    


class ImagenCreateView(CreateView):
    model = PresentacionProducto
    template_name = 'interfaceAdmin/adminFormularios/registrarImagen.html'
    form_class = CargarImagenForm
    success_url = reverse_lazy('listado_imagenes') 
    context_object_name='imagenes'

    def form_valid(self,form):
        imagenSelect= form.cleaned_data['imagen']
        form.save()
        mensaje=f'La Imegen({imagenSelect}) se registro correctamente'
        form_class= self.get_form_class()
        form=form_class
        context=self.get_context_data()
        context.update({'form':form,'mensaje':mensaje})
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Imagen'
        return context
    
class ImagenDeleteView(DeleteView):
    model = PresentacionProducto
    template_name = 'interfaceAdmin/adminFormularios/eliminarImagen.html'
    success_url = reverse_lazy('listado_imagenes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar Imagen'
        context["list_url"] = reverse_lazy('listado_imagenes')
        return context

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            ruta = 'media/' + str(self.object.imagen)
            if os.path.exists(ruta):
                os.remove(ruta)
            #Delegar a la clase padre la eliminacion como tambien que funcione la funcion
            return super().delete(request, *args, **kwargs)
        except Http404:
            return self.handle_no_permission()
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error deleting image: {e}")
            return self.handle_no_permission()

    def handle_no_permission(self):
        pk = self.kwargs.get('pk') #ruta de mi urls accediendo desde la vista
        return self.render_to_response({
            'r1': f'La imagen {pk} no existe o no se puede eliminar'
        })
    

def listadoProductos(request):
    productos = Producto.objects.filter(estado='ACTIVO').values(
        'id_producto', 'nombre', 'tipo', 'descripcion'
    ).annotate(
        stock=F('valor__stock'), 
        imagen=F('presentacionproducto__imagen'), 
        precio=F('valor__precio')
    )

    return render(request, 'interfaceAdmin/adminFormularios/listadoProductos.html', {'productos': productos})

class ImagenesListView(ListView):
    model= PresentacionProducto
    template_name='interfaceAdmin/adminFormularios/listadoDeImagenes.html'
    context_object_name='imagenes'

    def get_queryset(self):
        return PresentacionProducto.objects.all()
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Imagenes'
        return context
    
class ImagenesUpdateView(UpdateView):
    model=PresentacionProducto
    form_class=CargarImagenForm 
    template_name='interfaceAdmin/adminFormularios/registrarImagen.html'
    success_url= reverse_lazy('listado_imagenes')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Imagen'
        return context
    

    

class ProductoListView(ListView):
    model= Producto
    template_name='interfaceAdmin/adminFormularios/listadoDeProductos.html'
    context_object_name='productos'

    def get_queryset(self):
        return Producto.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Productos"
        return context
    
class ProductoUpdateView(UpdateView):
    model= Producto
    form_class= ProductoForm
    template_name='interfaceAdmin/adminFormularios/registrarProductos.html'
    success_url= reverse_lazy("listadoDeProductos")

class ProductoDeleteView(DeleteView):
        model= Producto
        template_name='interfaceAdmin/adminFormularios/eliminarProducto.html'
        success_url= reverse_lazy('listadoDeProductos')

        def get_context_data(self, **kwargs) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context["title"] = 'Eliminar Producto'
            context["list_url"] = reverse_lazy('listadoDeProductos')
            return context
        
class ClienteListView(ListView):
    model= Cliente
    template_name='interfaceAdmin/adminFormularios/listadoDeClientes.html'
    context_object_name='clientes'

    def get_queryset(self):
        return Cliente.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Clientes"
        return context

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
    form = IngredienteForm(request.POST)

    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            nombreSelect = form.cleaned_data['nombre']
            nombreIngrediente = Ingrediente.objects.filter(nombre=nombreSelect)
            if nombreIngrediente.exists():
                mensaje = 'El Ingrediente (' + str(nombreSelect) + ') ya existe'
            else:
                form.save()
                mensaje = 'El Ingrediente (' + str(nombreSelect) + ') se guardó correctamente'
                return redirect('listadoIngredientes')
        else:
            mensaje = 'Hay errores en el formulario.'
    else:
        mensaje = ''
    return render(request, 'interfaceAdmin/adminFormularios/registrarIngrediente.html', {'form': form, 'mensaje': mensaje})




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
    envios = Envio.objects.select_related('id_compra','id_estadoenvio').all()
    data = {
        'envios':envios
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

def pasteleria_tradicional(request):
    productos = Producto.objects.filter(tipo='Pastelería Tradicional', estado='ACTIVO')
    return render(request, 'interfaceCliente/pasteleria_tradicional.html', {'productos': productos})

def tortas_modernas(request):
    productos = Producto.objects.filter(tipo='Tortas Modernas', estado='ACTIVO')
    return render(request, 'interfaceCliente/tortas_modernas.html', {'productos': productos})

def panaderia(request):
    productos = Producto.objects.filter(tipo='Panadería', estado='ACTIVO')
    return render(request, 'interfaceCliente/panaderia.html', {'productos': productos})

def tortas_heladas(request):
    productos = Producto.objects.filter(tipo='Tortas Heladas', estado='ACTIVO')
    return render(request, 'interfaceCliente/tortas_heladas.html', {'productos': productos})

def bolleria(request):
    productos = Producto.objects.filter(tipo='Bollería', estado='ACTIVO')
    return render(request, 'interfaceCliente/bolleria.html', {'productos': productos})

def dulce_tentacion(request):
    productos = Producto.objects.filter(tipo='Dulce Tentación', estado='ACTIVO')
    return render(request, 'interfaceCliente/dulce_tentacion.html', {'productos': productos})

def cheesecake(request):
    productos = Producto.objects.filter(tipo='Cheesecake', estado='ACTIVO')
    return render(request, 'interfaceCliente/cheesecake.html', {'productos': productos})





def format_precio_clp(precio):
    return "{:,.0f}".format(precio).replace(",", ".")

@login_required
def detalleProducto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    form_carrito = DetalleCarritoForm(request.POST or None)
    form_calificacion = CalificacionForm(request.POST or None)
    calificaciones = Calificacion.objects.filter(id_producto=id_producto)
    valor = Valor.objects.filter(id_producto=id_producto).first()

    if request.method == 'POST':
        if 'agregar_carrito' in request.POST and form_carrito.is_valid():
            id_cliente = Cliente.objects.filter(email=request.user.email).first()
            if id_cliente:
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
            id_cliente = Cliente.objects.filter(email=request.user.email).first()
            if id_cliente:
                nueva_calificacion = form_calificacion.save(commit=False)
                nueva_calificacion.id_producto = producto
                nueva_calificacion.id_cliente = id_cliente
                nueva_calificacion.save()
                return redirect('detalleProducto', id_producto=id_producto)

    precio_formato_clp = "{:,.0f}".format(valor.precio).replace(",", ".") if valor else 'No Disponible'

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

