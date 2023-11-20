from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cliente/',views.seccion_cliente,name='seccion_cliente'),
]
