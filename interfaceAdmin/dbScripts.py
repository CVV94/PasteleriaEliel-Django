from django.shortcuts import render,redirect
from .models import Producto

def RegistrarPasteleriaTradicional(request):
    
    productos = [
    Producto(nombre='Primavera', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, PULPA DE MANGO Y SALSA DE FRUTILLA.', estado='Activo'),
    Producto(nombre='Banana Split', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA, CHIPS DE CHOCOLATE Y PLÁTANO PICADO CON TOQUES DE MANJAR.', estado='Activo'),
    Producto(nombre='Tres Leches', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA PASTELERA Y REMOJO DE TRES LECHES.', estado='Activo'),
    Producto(nombre='Moca', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA DE CAFÉ, DAMASCO Y NUEZ PICADA.', estado='Activo'),
    Producto(nombre='Mango', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA DE MANGO Y PULPA DE MANGO.', estado='Activo'),
    Producto(nombre='Piña Colada', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA SABOR A COCO, PIÑA PICADA Y CRENFIL DE COCO.', estado='Activo'),
    Producto(nombre='Amapola', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO CON SEMILLAS DE AMAPOLA, CREMA MANJAR NUEZ, SALSA DE FRAMBUESA Y MORA.', estado='Activo'),
    Producto(nombre='Siete Sabores', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, MIL HOJAS, BIZCOCHO DE CHOCOLATE, MANJAR, CREMA PASTELERA, GUINDA, FRAMBUESA, SALSA DE FRUTILLA DAMASCO Y MANGO.', estado='Activo'),
    Producto(nombre='Tiramisú', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, REMOJO DE CAFÉ', estado='Activo'),
    Producto(nombre='Manjar Durazno', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, MANJAR, DURAZNO PICADOS.', estado='Activo'),
    Producto(nombre='Delirio de mango', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, REMOJO DE TRES LECHES, LECHE DE COCO, RON MALIBU, CREMA DE MANGO Y PULPA DE MANGO.', estado='Activo'),
    Producto(nombre='Americana', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, BIZCOCHO DE CHOCOLATE, MANJAR, CREMA NUEZ CREMA CHANTILLY, SALSA DE FRUTILLA.', estado='Activo'),
    Producto(nombre='Amor', tipo='Pastelería Tradicional', descripcion='MIL HOJAS, BIZCOCHO BLANCO, MANJAR, CREMA PASTELERA, CREMA FRAMBUESA.', estado='Activo'),
    Producto(nombre='Choco Praliné', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE CHOCOLATE, CREMA DE ALMENDRA CON ESENCIA DE CARAMELO, TRUFA DE CHOCOLATE Y SALSA DE MORA.', estado='Activo'),
    Producto(nombre='Chocman', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE CHOCOLATE, MANJAR, CREMA Y TRUFA DE CHOCOLATE', estado='Activo'),
    Producto(nombre='Selva Negra ( Bizcocho )', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE CHOCOLATE, CREMA, Y SALSA DE GUINDA.', estado='Activo'),
    Producto(nombre='Red Velvet', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE TERCIOPELO ROJO RELLENO DE FROSTING DE VAINILLA.', estado='Activo'),
    Producto(nombre='Toffee', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE NUEZ, REMOJO DE TRES LECHES Y BIZCOCHO BLANCO.', estado='Activo'),
    Producto(nombre='Turrón', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE NUEZ, MANJAR CREMA, DISCO DE MERENGUE SECO Y CREMA PASTELERA', estado='Activo'),
    Producto(nombre='Pompadour', tipo='Pastelería Tradicional', descripcion='HOJARASCA RELLENA CON MANJAR Y CREMA SABOR A PLÁTANO', estado='Activo'),
    Producto(nombre='Mocca 3 leches', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, REMOJO DE 3 LECHES CON CAFÈ Y MANJAR CREMA SABOR A CAFÈ.', estado='Activo'),
    Producto(nombre='Torta de Oreo', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE CHOCOLATE RELLENA DE TRUFA, QUESO CREMA, CREMA Y GALLETA OREO', estado='Activo'),
    Producto(nombre='Mil Hojas', tipo='Pastelería Tradicional', descripcion='RELLENO A ELECCIÓN CREMA DE : SALSA DE FRUTILLA , LUCUMA , FRAMBUESA , MANGO , MANJAR NUEZ , MANJAR COCO . CREMA PASTELERA PUEDE IR CUBIERTA CON MANJAR O CREMA, PUEDE LLEVAR NUEZ, MIGA O COCO .', estado='Activo'),
    Producto(nombre='Avellana Lúcuma', tipo='Pastelería Tradicional', descripcion='BIZCOCHO CHOCOLATE, CREMA, LÚCUMA, MANJAR', estado='Activo'),
    Producto(nombre='Delirio de lúcuma', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, CREMA, LÚCUMA, REMOJO DE TRES Y LECHES', estado='Activo'),
    Producto(nombre='Holandesa', tipo='Pastelería Tradicional', descripcion='HOJARASCA, CREMA PASTELERA, MANJAR Y FRAMBUESA', estado='Activo'),
    Producto(nombre='Mango Frutilla', tipo='Pastelería Tradicional', descripcion='MANGO FRUTILLA, REMOJO DE 3 LECHES, BIZCOCHO BLANCO.', estado='Activo'),
    Producto(nombre='Choco Torta', tipo='Pastelería Tradicional', descripcion='BIZCOCHO DE CHOCOLATE , CREMA DE FRAMBUESA, CREMA MORA Y MANJAR.', estado='Activo'),
    Producto(nombre='Dominga', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO , REMOJO 3 LECHE , RELLENA DE CREMA PASTELERA, DURAZNO, MANGO Y CREMA', estado='Activo'),
    Producto(nombre='Tropical', tipo='Pastelería Tradicional', descripcion='BIZCOCHO BLANCO, REMOJO DE COCO TRES LECHE, RELLENA DE PIÑA EN TROZO, CREMA DE COCO CON PULPA DE MARACUYÁ Y MANGO.', estado='Activo'),
    ]

    Producto.objects.bulk_create(productos)
    return redirect('scripts')