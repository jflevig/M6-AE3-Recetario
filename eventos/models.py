from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(default=date.today)
    lugar = models.CharField(max_length=100)

    autor_evento = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='eventos_creados'
    )

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"