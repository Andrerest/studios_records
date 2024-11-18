from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Create a model for Music Genres
class GeneroMusical(models.Model):
    nombre_genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_genero

# Create a model for Venues (Ubicaciones)
class Ubicacion(models.Model):
    nombre_venue = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_venue

# Create a model for Events (Eventos)
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    capacidad = models.PositiveIntegerField()
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_evento

# Create a model for Ticket Types (Tipos de Tickets)
class TipoDeTicket(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_ticket = models.CharField(max_length=50)
    moneda = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_ticket

# Create a model for Artists (Artistas)
class Artista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    foto = models.URLField(max_length=255, blank=True)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    enlaces_sociales = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
# Create a model for Schedules (Horarios)
class Horario(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_performance = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f'{self.artista.nombre} - {self.fecha_performance}'

# Create a model for Attendees (Asistencia)
class Asistente(models.Model):
    identificacion = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=100)
    numero_telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.primer_nombre} {self.apellido}'

# Create a model for Tickets
class Ticket(models.Model):
    asistencia = models.ForeignKey(Asistente, on_delete=models.CASCADE)
    tipo_de_ticket = models.ForeignKey(TipoDeTicket, on_delete=models.CASCADE)
    fecha_compra = models.DateField()

    def __str__(self):
        return f'Ticket for {self.asistencia} to {self.tipo_de_ticket.evento.nombre_evento}'
