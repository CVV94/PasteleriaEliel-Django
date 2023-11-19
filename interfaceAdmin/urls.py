from django.urls import path
from . import views
urlpatterns = [
    path('interface/',views.interfaceAdmin,name='interfazAdministrador'),
    path('registrar/producto',views.registrarProducto,name='registrarProducto'),
    path('registrar/valor',views.registrarValor,name='registrarPrecio'),
    path('registrar/imagen',views.registrarImagen,name='registrarImagen'),
    path('listado/productos',views.listadoProductos,name='listadoProductos'),
 
]
