from django.shortcuts import render, redirect
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'index.html', context)

def pagar(request):
    if request.method == 'POST':
        codigo_producto = request.POST['codigoDeProducto']
        producto = Producto.objects.get(codigo_producto=codigo_producto)
        producto.stock -= 1
        producto.numero_comprados += 1
        producto.save()
        return redirect('index')
    return redirect('index')