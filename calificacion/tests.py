from django.test import TestCase
from django.urls import reverse
from .models import Calificacion

class CalificacionTests(TestCase):
    def test_crear_calificacion(self):
        cal = Calificacion.objects.create(
            nombre="María",
            comentario="Muy bueno",
            calificacion=9,
        )
        self.assertEqual(cal.calificacion, 9)

    def test_vista_lista_calificaciones(self):
        response = self.client.get(reverse('calificacion:lista'))
        self.assertEqual(response.status_code, 200)
