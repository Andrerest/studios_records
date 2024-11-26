from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Modelo para Ubicaciones
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, {self.pais}"

    class Meta:
        verbose_name_plural = "Ubicaciones"

# Modelo para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, related_name="eventos")
    capacidad = models.PositiveIntegerField()
    es_publico = models.BooleanField(default=True)
    precio_entrada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        help_text="Precio de entrada al evento. Déjelo en 0 para eventos gratuitos."
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["fecha_inicio"]
        verbose_name_plural = "Eventos"

# Modelo para Registraciones
class Registracion(models.Model):
    evento = models.ForeignKey(Evento, related_name='registraciones', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='registraciones', on_delete=models.CASCADE)
    fecha_registrado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[("pendiente", "Pendiente"), ("confirmada", "Confirmada"), ("cancelada", "Cancelada")],
        default="pendiente"
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.evento.nombre}"

    class Meta:
        unique_together = ('evento', 'usuario')  # Evitar duplicados

# Modelo para Categorías de Eventos
class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    eventos = models.ManyToManyField(Evento, related_name="categorias", blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías de Eventos"
