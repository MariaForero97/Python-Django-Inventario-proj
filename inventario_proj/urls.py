from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('almacen/', include('almacen.urls')),
    path('calificacion/', include('calificacion.urls')),
]

handler404 = "inventario_proj.views.custom_404"