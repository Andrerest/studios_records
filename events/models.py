from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to="eventos/", blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    entrada_general = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        help_text="Precio de entrada al evento. Déjelo en 0 para eventos gratuitos."
    )
    entrada_vip = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        help_text="Precio de entrada al evento. Déjelo en 0 para eventos gratuitos."
    )
    cantidad_general = models.PositiveIntegerField(default=0, help_text="Cantidad de entradas generales disponibles")
    cantidad_vip = models.PositiveIntegerField(default=0, help_text="Cantidad de entradas VIP disponibles")

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["fecha_inicio"]
        verbose_name_plural = "Eventos"


class Ticket(models.Model):
    event = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='tickets')
    type = models.CharField(max_length=100)  # e.g., VIP, General Admission
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')  # Optional

    def __str__(self):
        return f"{self.type} - {self.price} {self.currency}"

# Modelo para Registraciones
class Registracion(models.Model):
    evento = models.ForeignKey(Evento, related_name='registraciones', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='registraciones', on_delete=models.CASCADE)
    fecha_registrado = models.DateTimeField(auto_now_add=True)
    tipo_entrada = models.CharField(
        max_length=20,
        choices=[("general", "General"), ("vip", "VIP")],
        default="general"
    )
    estado = models.CharField(
        max_length=20,
        choices=[("pendiente", "Pendiente"), ("confirmada", "Confirmada"), ("cancelada", "Cancelada")],
        default="pendiente"
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.evento.nombre} ({self.tipo_entrada})"
    
    class Meta:
        unique_together = ('evento', 'usuario', 'tipo_entrada')  # Prevent multiple registrations for the same event and ticket type by the same user
