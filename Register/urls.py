from django.urls import path
from . import views
urlpatterns = [
    path('registro/cliente', views.registro_cliente, name='registro_cliente'),
    path('login/cliente', views.login_cliente, name='login_cliente'),
    path('logout/cliente', views.cerrar_sesion, name='cerrar_sesion'),
]
