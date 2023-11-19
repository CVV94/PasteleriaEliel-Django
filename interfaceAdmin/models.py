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