from django.shortcuts import render, get_object_or_404
from .models import categoria, productos, clientes, venta, Detalleventa


def index(request):
    return render(request, 'tienda/index.html')


def lista_categorias(request):
    lista = categoria.objects.all()

    return render(
        request,
        'tienda/lista_categorias.html',
        {'lista': lista}
    )


def lista_productos(request):
    lista = productos.objects.select_related('categoria').all()

    return render(
        request,
        'tienda/lista_productos.html',
        {'lista': lista}
    )


def lista_clientes(request):
    lista = clientes.objects.all()

    return render(
        request,
        'tienda/lista_clientes.html',
        {'lista': lista}
    )


def lista_venta(request):
    lista = venta.objects.select_related('cliente').all()

    return render(
        request,
        'tienda/lista_venta.html',
        {'lista': lista}
    )


def lista_detalle_ventas(request):
    lista = Detalleventa.objects.select_related(
        'venta',
        'producto',
        'venta__cliente'
    ).all()

    return render(
        request,
        'tienda/lista_detalle_ventas.html',
        {'lista': lista}
    )