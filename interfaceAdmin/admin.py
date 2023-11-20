from django.contrib import admin
from .models import Producto,PresentacionProducto,Valor
# Register your models here.

admin.site.register(Producto),
admin.site.register(PresentacionProducto),
admin.site.register(Valor)