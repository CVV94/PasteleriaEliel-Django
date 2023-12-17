from django.contrib import admin
from .models import Producto,PresentacionProducto,Valor,Cliente,Estadopago,Compra,CarritoCompra,DetalleCarritoCompraProducto,Envio,Estadoenvio
# Register your models here.

admin.site.register(Producto),
admin.site.register(PresentacionProducto),
admin.site.register(Valor),
admin.site.register(Cliente),
admin.site.register(Estadopago),
admin.site.register(Compra),
admin.site.register(CarritoCompra),
admin.site.register(DetalleCarritoCompraProducto),
admin.site.register(Envio),
admin.site.register(Estadoenvio),