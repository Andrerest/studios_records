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


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=20)
    ticket_quantity = models.PositiveIntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaction {self.id} - {self.evento.nombre} - {self.status}"