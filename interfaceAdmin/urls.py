from django.urls import path
from . import views
from .views import ProductoListView,ProductoUpdateView,ProductoCreateView,ProductoDeleteView,ImagenesListView,ImagenesUpdateView,ImagenCreateView,ImagenDeleteView,ClienteListView,ValorCreateView
from . import dbScripts
urlpatterns = [
    path('interface/',views.interfaceAdmin,name='interfazAdministrador'),
    path('registrar/producto',ProductoCreateView.as_view(),name='registrarProducto'),
    path('registrar/valor',ValorCreateView.as_view(),name='registrarPrecio'),
    path('registrar/imagen',ImagenCreateView.as_view(),name='registrar_imagen'),
    path('listado/productos',views.listadoProductos,name='listadoProductos'),
    path('scripts/productos',dbScripts.scriptsRegistrarProductos,name='scriptsRegistrarProductos'),
    path('scripts/Registros',dbScripts.scriptsRegistros,name='scripts'),
    path('listado/producto',ProductoListView.as_view(),name='listadoDeProductos'),
    path('listado/imagenes',ImagenesListView.as_view(),name='listado_imagenes'),
    path('listado/cliente',ClienteListView.as_view(),name='listado_clientes'),
    path('editar/imagen/<int:pk>/',ImagenesUpdateView.as_view(),name='editar_imagenes'),
    path('actualizar/producto/<int:pk>/',ProductoUpdateView.as_view(),name='actualizar_producto'),
    path('eliminar/producto/<int:pk>/',ProductoDeleteView.as_view(),name='eliminar_producto'),
    path('eliminar/imagen/<int:pk>/',ImagenDeleteView.as_view(),name='eliminar_imagen'),

    path('listado/ingredientes',views.listadoIngredientes, name='listadoIngredientes'),
    path('registrar/ingrediente', views.registrarIngrediente, name='registrarIngrediente'),
    path('editarIngrediente/<int:id_ingrediente>', views.editarIngrediente, name='editarIngrediente'),
    path('eliminarIngrediente/<int:id_ingrediente>',views.eliminarIngrediente, name='eliminarIngrediente'),

    path('listado/proveedores',views.listadoProveedores, name='listadoProveedores'),
    path('registrar/proveedor', views.registrarProveedor, name='registrarProveedor'),
    path('editarProveedor/<int:id_proveedor>', views.editarProveedor, name='editarProveedor'),
    path('eliminarProveedor/<int:id_proveedor>',views.eliminarProveedor, name='eliminarProveedor'),

    path('listado/envios',views.listadoEnvios, name='listadoEnvios'),
    path('edit-envios/<int:id_envio>/', views.editEnvios, name='edit_envios'),
    
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
