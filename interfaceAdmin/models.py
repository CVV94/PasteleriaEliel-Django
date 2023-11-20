from django.db import models

# Create your models here.
class Producto(models.Model):
    Estados=[('ACTIVO','activo'),('DESACTIVO','desactivo')]
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE',max_length=20)
    tipo = models.CharField(db_column='TIPO',max_length=20)
    estado = models.CharField(db_column='ESTADO',max_length=20,choices=Estados,default='activo')
    descripcion= models.CharField(db_column='DESCRIPCION',max_length=250)
    
    class Meta:
        managed = True
        db_table = 'Producto'
    def __str__(self):
        return f'{self.id_producto}'

class PresentacionProducto(models.Model):
    id_presentacion = models.AutoField(db_column='ID_PRESENTACION',primary_key=True)
    imagen= models.ImageField(db_column='IMAGEN',upload_to='img_producto/')
    id_producto = models.ForeignKey(Producto,models.DO_NOTHING,db_column='ID_PRODUCTO')

    class Meta:
        managed = True
        db_table = 'PresentacionProducto'

class Valor(models.Model):
    id_valor = models.AutoField(primary_key=True,db_column='ID_VALOR')
    cantidad_de_Personas = models.IntegerField(db_column='CANTIDAD_DE_PERSONAS')
    precio = models.DecimalField(db_column='PRECIO',decimal_places=2,max_digits=9)
    stock = models.IntegerField(db_column='STOCK')
    id_producto = models.ForeignKey(Producto,models.DO_NOTHING,db_column='ID_PRODUCTO')

    class Meta:
        managed = True
        db_table = 'Valor'

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(db_column='ID_INGREDIENTE', primary_key=True)  
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO')  
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='ID_PROVEEDOR')  
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=250)  
    unidad_medida = models.CharField(db_column='UNIDAD_MEDIDA', max_length=20)  
    precio = models.IntegerField(db_column='PRECIO')  
    stock = models.IntegerField(db_column='STOCK')  

    class Meta:
        managed = True
        db_table = 'ingrediente'

class Proveedor(models.Model):
    id_proveedor = models.AutoField(db_column='ID_PROVEEDOR', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  
    direccion = models.CharField(db_column='DIRECCION', max_length=60)  
    telefono = models.IntegerField(db_column='TELEFONO')  
    web = models.CharField(db_column='WEB', max_length=250, blank=True, null=False)  

    class Meta:
        managed = True
        db_table = 'proveedor'

class Calificacion(models.Model):
    id_valoracion = models.AutoField(db_column='ID_VALORACION', primary_key=True)  
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ID_CLIENTE')  
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO')  
    calificacion = models.IntegerField(db_column='CALIFICACION')  
    titulo = models.CharField(db_column='TITULO', max_length=20)  
    comentario = models.CharField(db_column='COMENTARIO', max_length=250)  

    class Meta:
        managed = True
        db_table = 'calificacion'


class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='ID_CLIENTE', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  
    apellido = models.CharField(db_column='APELLIDO', max_length=20)  
    email = models.EmailField(db_column='EMAIL', max_length=60)  
    telefono = models.IntegerField(db_column='TELEFONO', null=False)  

    class Meta:
        managed = True
        db_table = 'cliente'
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)
    

class CarritoCompra(models.Model):
    id_carrito = models.AutoField(db_column='ID_CARRITO', primary_key=True)  
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ID_CLIENTE')  
    costo_envio = models.FloatField(db_column='COSTO_ENVIO')  
    sub_total = models.FloatField(db_column='SUB_TOTAL')  
    iva = models.FloatField(db_column='IVA')  

    class Meta:
        managed = True
        db_table = 'carritocompra'

class DetalleCarritoCompraProducto(models.Model):
    id_detalle = models.AutoField(db_column='ID_DETALLE', primary_key=True)  
    id_carrito = models.ForeignKey(CarritoCompra, models.DO_NOTHING, db_column='ID_CARRITO')  
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO')  
    cantidad = models.IntegerField(db_column='CANTIDAD')  
    precio_unitario = models.FloatField(db_column='PRECIO_UNITARIO')  
    tipo_entrega = models.CharField(db_column='TIPO_ENTREGA', max_length=50)  

    class Meta:
        managed = True
        db_table = 'detalle_carritocompra_producto'

class Compra(models.Model):
    id_compra = models.AutoField(db_column='ID_COMPRA', primary_key=True)  
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_CLIENTE')  
    id_carrito = models.ForeignKey(CarritoCompra, models.DO_NOTHING, db_column='ID_CARRITO')  
    id_estadopago = models.ForeignKey('Estadopago', models.DO_NOTHING, db_column='ID_ESTADOPAGO')  
    fecha_compra = models.DateField(db_column='FECHA_COMPRA')  
    total_compra = models.IntegerField(db_column='TOTAL_COMPRA',null=False)  
    direccion = models.CharField(db_column='DIRECCION', max_length=60)  

    class Meta:
        managed = True
        db_table = 'compra'


class Envio(models.Model):
    id_envio = models.AutoField(db_column='ID_ENVIO', primary_key=True)  
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='ID_COMPRA')  
    id_estadoenvio = models.ForeignKey('Estadoenvio', models.DO_NOTHING, db_column='ID_ESTADOENVIO')  
    fecha_envio = models.DateField(db_column='FECHA_ENVIO')  
    fecha_entrega = models.DateField(db_column='FECHA_ENTREGA')  

    class Meta:
        managed = True
        db_table = 'envio'


class Estadoenvio(models.Model):
    id_estadoenvio = models.AutoField(db_column='ID_ESTADOENVIO', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  

    class Meta:
        managed = True
        db_table = 'estadoenvio'


class Estadopago(models.Model):
    id_estadopago = models.AutoField(db_column='ID_ESTADOPAGO', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  

    class Meta:
        managed = True
        db_table = 'estadopago'