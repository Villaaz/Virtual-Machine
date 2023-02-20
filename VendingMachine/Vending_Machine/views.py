from django.shortcuts import render, redirect
from .models import Producto
from django.views import generic

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

class ProductListView(generic.ListView):
    model = Producto

class ProductDetailView(generic.DetailView):
    model = Producto

class ProductEditView(generic.UpdateView):
    model = Producto
    template_name_suffix = "_edit"
    fields = ['codigo_producto', 'nombre_producto', 'precio', 'stock', 'num_comprados']

def zonaAdmin(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'parteAdmin.html', context=context)

def editPrecio(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'edit_precio.html', context=context)

def alertarProveedor(request):
    context = {}
    return render(request, 'alertar_proveedor.html', context=context)

def verEstadisticas(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'ver_estadisticas.html', context=context)