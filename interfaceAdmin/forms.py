from django import forms
from .models import Producto,PresentacionProducto,Valor, Proveedor, Ingrediente, Compra, Envio, Estadoenvio, Calificacion

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


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['titulo', 'comentario', 'calificacion']  # Ajusta los campos según sea necesario
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Título'}),
            'comentario': forms.Textarea(attrs={'cols': 40, 'rows': 5, 'placeholder': 'Comentario'}),
            'calificacion': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
