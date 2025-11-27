from django.db import models

class Calificacion(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField(blank=True)
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.calificacion}"
