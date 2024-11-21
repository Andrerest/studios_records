from django.db import models
from django.contrib.auth.models import User


# Modelo para Ubicaciones
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

# Modelo para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name="eventos")
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["fecha_inicio"]
        verbose_name_plural = "Eventos"

# Modelo para Tipos de Tickets
class TipoDeTicket(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="tipos_de_tickets")
    nombre = models.CharField(max_length=50)
    moneda = models.CharField(max_length=3)  # ISO 4217 (e.g., USD, EUR)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.evento.nombre}"

# Modelo para Artistas
class Artista(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    foto = models.ImageField(upload_to="artistas/", blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


# Modelo para Horarios de Eventos
class Horario(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="horarios")
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="presentaciones")
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.artista.nombre} - {self.evento.nombre} ({self.fecha})"

