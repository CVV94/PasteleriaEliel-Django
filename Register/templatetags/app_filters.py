from django import template

register = template.Library()

@register.filter(name='precio_formateadoVenta')
def precio_formateado_venta(value):
    if value is None:
        return 'None'
    return "${:,.0f}".format(value).replace(',', '.')

@register.filter(name='precio_formateadoDetalleVenta')
def precio_formateado_detalle_venta(value):
    if value is None:
        return 'None'
    return "${:,.0f}".format(value).replace(',', '.')