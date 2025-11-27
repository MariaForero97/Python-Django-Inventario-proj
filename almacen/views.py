from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Product, Category
from .forms import ProductForm, CategoryForm


# 🏠 Página principal
def home(request):
    qs = Product.objects.select_related('category').order_by('-created_at')
    q = request.GET.get('q')
    if q:
        qs = qs.filter(name__icontains=q)
    context = {'products': qs}
    return render(request, 'almacen/home.html', context)


# 📦 Detalle del producto
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'almacen/product_detail.html', {'product': product})


# 📂 Productos por categoría 
def products_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return render(request, 'almacen/category_products.html', {
        'category': category,
        'products': products
    })


# ➕ Crear producto
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Producto creado correctamente.")
            return redirect('almacen:home')
    else:
        form = ProductForm()
    return render(request, 'almacen/product_form.html', {'form': form, 'action': 'Crear'})


# ✏️ Editar producto
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Producto actualizado correctamente.")
            return redirect('almacen:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'almacen/product_form.html', {'form': form, 'action': 'Editar'})


# ❌ Eliminar producto
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "🗑️ Producto eliminado correctamente.")
        return redirect('almacen:home')
    return render(request, 'almacen/product_confirm_delete.html', {'product': product})


# ➕ Crear categoría
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "📁 Categoría creada correctamente.")
            return redirect('almacen:home')
    else:
        form = CategoryForm()
    return render(request, 'almacen/category_form.html', {'form': form})


# 📁 Productos por categoría 
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.product_set.all()
    return render(request, 'almacen/category_products.html', {
        'category': category,
        'products': products
    })


# --- Vistas genéricas (CBV) sencillas ---

class ProductListView(ListView):
    model = Product
    template_name = "almacen/product_list_cbv.html"
    context_object_name = "products"



class ProductDetailView(DetailView):
    model = Product
    template_name = "almacen/product_detail_cbv.html"
    context_object_name = "product"


# 🚨 Controlador global para error 404
def custom_404(request, exception=None):
    """Vista personalizada para manejar el error 404"""
    return render(request, '404.html', status=404)
