from django import forms
from .models import Producto,PresentacionProducto,Valor, Proveedor, Ingrediente, Compra, Envio, Estadoenvio

class ProductoForm(forms.ModelForm):
    class Meta:
        Estados=[('ACTIVO','activo'),('DESACTIVO','desactivo')]
        model = Producto
        fields= ('__all__')
        widgets={
            'nombre':forms.TextInput(attrs={'class':'input'}),
            'tipo':forms.TextInput(attrs={'class':'input'}),
            'estado':forms.Select(choices=Estados),
            'descripcion':forms.Textarea(attrs={'cols':56,'rows':20})
        }
    
        
class CargarImagenForm(forms.ModelForm):
    class Meta:
        model=PresentacionProducto
        fields=('__all__')


class ValorForm(forms.ModelForm):
    class Meta:
        model=Valor
        fields=('__all__')


class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('__all__')


class IngredienteForm(forms.ModelForm):
    class Meta:
        model=Ingrediente
        fields=('__all__')


class CompraForm(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('__all__')


class EnvioForm(forms.ModelForm):
    class Meta:
        model=Envio
        fields=('__all__')