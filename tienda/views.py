# tienda/views.py

from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categories = Categoria.objects.all()
    context = {'product_list': product_list, 'categories': categories}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categories = Categoria.objects.all()
    return render(request, 'producto.html', {'producto': producto, 'categories': categories})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    products = Producto.objects.filter(categoria=categoria)
    categories = Categoria.objects.all()
    return render(request, 'categoria.html', {'categoria': categoria, 'products': products, 'categories': categories})