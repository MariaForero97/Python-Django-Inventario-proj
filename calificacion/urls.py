from django.urls import path
from . import views

app_name = 'calificacion'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_calificaciones, name='lista'),
    path('firebase/', views.lista_firebase, name='lista_firebase'),
]
