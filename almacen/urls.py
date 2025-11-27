from django.urls import path
from . import views

app_name = 'almacen'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:id>/', views.products_by_category, name='products_by_category'),
    path('productos_cbv/', views.ProductListView.as_view(), name='product_list_cbv'),
    path('producto_cbv/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail_cbv'),
]
