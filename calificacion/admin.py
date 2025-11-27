from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion')
    search_fields = ('nombre',)
    list_filter = ('calificacion',)
