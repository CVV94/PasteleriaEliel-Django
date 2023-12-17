from django.urls import path
from . import views
from . import dbScripts
urlpatterns = [
    path('interface/',views.interfaceAdmin,name='interfazAdministrador'),
    path('registrar/producto',views.registrarProducto,name='registrarProducto'),
    path('registrar/valor',views.registrarValor,name='registrarPrecio'),
    path('registrar/imagen',views.registrarImagen,name='registrarImagen'),
    path('listado/productos',views.listadoProductos,name='listadoProductos'),
    path('scripts/productos',dbScripts.scriptsRegistrarProductos,name='scriptsRegistrarProductos'),
    path('scripts/Registros',dbScripts.scriptsRegistros,name='scripts'),

    path('listado/ingredientes',views.listadoIngredientes, name='listadoIngredientes'),
    path('registrar/ingrediente', views.registrarIngrediente, name='registrarIngrediente'),
    path('editarIngrediente/<int:id_ingrediente>', views.editarIngrediente, name='editarIngrediente'),
    path('eliminarIngrediente/<int:id_ingrediente>',views.eliminarIngrediente, name='eliminarIngrediente'),

    path('listado/proveedores',views.listadoProveedores, name='listadoProveedores'),
    path('registrar/proveedor', views.registrarProveedor, name='registrarProveedor'),
    path('editarProveedor/<int:id_proveedor>', views.editarProveedor, name='editarProveedor'),
    path('eliminarProveedor/<int:id_proveedor>',views.eliminarProveedor, name='eliminarProveedor'),

    path('listado/envios',views.listadoEnvios, name='listadoEnvios'),
    path('registrar/envio', views.registrarEnvio, name='registrarEnvio'),
    path('editarEnvio/<int:id_envio>', views.editarEnvio, name='editarEnvio'),
    path('eliminarEnvio/<int:id_envio>',views.eliminarEnvio, name='eliminarEnvio'),

    path('listado/compras',views.listadoCompras, name='listadoCompras'),
    path('registrar/compra', views.registrarCompra, name='registrarCompra'),
    path('editarCompra/<int:id_compra>', views.editarCompra, name='editarCompra'),
    path('eliminarCompra/<int:id_compra>',views.eliminarCompra, name='eliminarCompra'),

    path('producto/<int:id_producto>/',views.detalleProducto, name='detalleProducto'),
    path('descripcionCarrito/',views.descripcionCarrito, name='descripcionCarrito'),
    path('carta/',views.listadoProductosCarta, name='carta'),
]
