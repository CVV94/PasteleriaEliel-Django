from pyexpat.errors import messages
from typing import Any
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import ProductoForm,CargarImagenForm,ValorForm, ProveedorForm, IngredienteForm, EnvioForm, CompraForm
from .models import Producto, Proveedor, Ingrediente, Compra, Envio, Estadoenvio, Cliente, CarritoCompra, Estadopago, PresentacionProducto,Valor
from django.db.models import F
from django.urls import reverse_lazy
import os
from django.http import Http404

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