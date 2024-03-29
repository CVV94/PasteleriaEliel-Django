# Generated by Django 4.2.7 on 2024-02-06 19:59

from django.db import migrations, models
import django.db.models.deletion
import interfaceAdmin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompra',
            fields=[
                ('id_carrito', models.AutoField(db_column='ID_CARRITO', primary_key=True, serialize=False)),
                ('costo_envio', models.FloatField(db_column='COSTO_ENVIO')),
                ('sub_total', models.FloatField(db_column='SUB_TOTAL')),
                ('iva', models.FloatField(db_column='IVA')),
            ],
            options={
                'db_table': 'carritocompra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(db_column='ID_CLIENTE', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=20)),
                ('apellido', models.CharField(db_column='APELLIDO', max_length=20)),
                ('email', models.EmailField(db_column='EMAIL', max_length=60)),
                ('telefono', models.IntegerField(db_column='TELEFONO')),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(db_column='ID_COMPRA', primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(db_column='FECHA_COMPRA')),
                ('total_compra', models.IntegerField(db_column='TOTAL_COMPRA')),
                ('direccion', models.CharField(db_column='DIRECCION', max_length=60)),
                ('id_carrito', models.ForeignKey(db_column='ID_CARRITO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.carritocompra')),
                ('id_cliente', models.ForeignKey(db_column='ID_CLIENTE', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.cliente')),
            ],
            options={
                'db_table': 'compra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estadoenvio',
            fields=[
                ('id_estadoenvio', models.AutoField(db_column='ID_ESTADOENVIO', primary_key=True, serialize=False)),
                ('nombre', models.CharField(choices=[('P', 'Pendiente'), ('E', 'En camino'), ('R', 'Recibido')], db_column='NOMBRE', default='P', max_length=8)),
            ],
            options={
                'db_table': 'estadoenvio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estadopago',
            fields=[
                ('id_estadopago', models.AutoField(db_column='ID_ESTADOPAGO', primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=False)),
                ('detalles_pago', models.CharField(blank=True, max_length=200, null=True)),
                ('estado_pago', models.CharField(choices=[('P', 'Pendiente'), ('S', 'Exitoso'), ('F', 'Fallido')], db_column='ESTADO_PAGO', default='P', max_length=10)),
            ],
            options={
                'db_table': 'estadopago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='ID_PRODUCTO', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=100)),
                ('tipo', models.CharField(db_column='TIPO', max_length=100)),
                ('estado', models.CharField(choices=[('ACTIVO', 'activo'), ('DESACTIVO', 'desactivo')], db_column='ESTADO', default='activo', max_length=20)),
                ('descripcion', models.CharField(db_column='DESCRIPCION', max_length=250)),
            ],
            options={
                'db_table': 'Producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(db_column='ID_PROVEEDOR', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=20)),
                ('direccion', models.CharField(db_column='DIRECCION', max_length=60)),
                ('telefono', models.IntegerField(db_column='TELEFONO')),
                ('web', models.CharField(blank=True, db_column='WEB', max_length=250)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id_valor', models.AutoField(db_column='ID_VALOR', primary_key=True, serialize=False)),
                ('cantidad_de_Personas', models.IntegerField(db_column='CANTIDAD_DE_PERSONAS')),
                ('precio', models.DecimalField(db_column='PRECIO', decimal_places=2, max_digits=9)),
                ('stock', models.IntegerField(db_column='STOCK')),
                ('id_producto', models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='valores', to='interfaceAdmin.producto')),
            ],
            options={
                'db_table': 'Valor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PresentacionProducto',
            fields=[
                ('id_presentacion', models.AutoField(db_column='ID_PRESENTACION', primary_key=True, serialize=False)),
                ('imagen', models.ImageField(db_column='IMAGEN', upload_to='img_producto/', validators=[interfaceAdmin.models.validate_image_file_extension])),
                ('id_producto', models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='presentaciones', to='interfaceAdmin.producto')),
            ],
            options={
                'db_table': 'PresentacionProducto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_ingrediente', models.AutoField(db_column='ID_INGREDIENTE', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=20)),
                ('descripcion', models.CharField(db_column='DESCRIPCION', max_length=250)),
                ('unidad_medida', models.CharField(db_column='UNIDAD_MEDIDA', max_length=20)),
                ('precio', models.IntegerField(db_column='PRECIO')),
                ('stock', models.IntegerField(db_column='STOCK')),
                ('id_producto', models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.producto')),
                ('id_proveedor', models.ForeignKey(db_column='ID_PROVEEDOR', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.proveedor')),
            ],
            options={
                'db_table': 'ingrediente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id_envio', models.AutoField(db_column='ID_ENVIO', primary_key=True, serialize=False)),
                ('fecha_envio', models.DateField(db_column='FECHA_ENVIO')),
                ('fecha_entrega', models.DateField(db_column='FECHA_ENTREGA')),
                ('recibido_por', models.CharField(blank=True, max_length=200, null=True)),
                ('rut', models.CharField(max_length=10)),
                ('id_compra', models.ForeignKey(db_column='ID_COMPRA', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.compra')),
                ('id_estadoenvio', models.ForeignKey(db_column='ID_ESTADOENVIO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.estadoenvio')),
            ],
            options={
                'db_table': 'envio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleCarritoCompraProducto',
            fields=[
                ('id_detalle', models.AutoField(db_column='ID_DETALLE', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='CANTIDAD')),
                ('precio_unitario', models.FloatField(db_column='PRECIO_UNITARIO')),
                ('tipo_entrega', models.CharField(db_column='TIPO_ENTREGA', max_length=50)),
                ('id_carrito', models.ForeignKey(db_column='ID_CARRITO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.carritocompra')),
                ('id_producto', models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.producto')),
            ],
            options={
                'db_table': 'detalle_carritocompra_producto',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='id_estadopago',
            field=models.ForeignKey(db_column='ID_ESTADOPAGO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.estadopago'),
        ),
        migrations.AddField(
            model_name='carritocompra',
            name='id_cliente',
            field=models.ForeignKey(db_column='ID_CLIENTE', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.cliente'),
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_valoracion', models.AutoField(db_column='ID_VALORACION', primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField(db_column='CALIFICACION')),
                ('titulo', models.CharField(db_column='TITULO', max_length=20)),
                ('comentario', models.CharField(db_column='COMENTARIO', max_length=250)),
                ('id_cliente', models.ForeignKey(db_column='ID_CLIENTE', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.cliente')),
                ('id_producto', models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, to='interfaceAdmin.producto')),
            ],
            options={
                'db_table': 'calificacion',
                'managed': True,
            },
        ),
    ]
