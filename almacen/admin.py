from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Buscar categorías por nombre


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'quantity')
    list_filter = ('category',)              # Filtro lateral por categoría
    search_fields = ('name', 'sku')          # Búsqueda por nombre o SKU
    list_editable = ('price', 'quantity')    # Editar precio y cantidad en la lista
