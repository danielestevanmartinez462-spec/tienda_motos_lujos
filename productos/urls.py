from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),

    path(
        'categorias/',
        views.lista_categorias,
        name='lista_categorias'
    ),

    path(
        'productos/',
        views.lista_productos,
        name='lista_productos'
    ),

    path(
        'clientes/',
        views.lista_clientes,
        name='lista_clientes'
    ),

    path(
        'ventas/',
        views.lista_venta,
        name='lista_venta'
    ),

    path(
        'detalle-ventas/',
        views.lista_detalle_ventas,
        name='lista_detalle_ventas'
    ),
]