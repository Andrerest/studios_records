from django.db import models
from django.contrib.auth.models import User

class Artista(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100, unique=True)
    foto = models.ImageField(upload_to="artistas/", blank=True)
    descripcion = models.TextField(blank=True)
    seguidores = models.ManyToManyField(User, related_name="seguidores")
    nacionalidad = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Date of birth

    def __str__(self):
        return self.nombre

    def total_seguidores(self):
        print("Seguidores: ", self.seguidores.count() )
        return self.seguidores.count() if self.seguidores.exists() else 0



class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="albums")
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    portada = models.ImageField(upload_to="albums/", blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} by {self.artista.nombre}"

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="canciones")
    titulo = models.CharField(max_length=100)
    duracion = models.TimeField() 
    archivo_audio = models.FileField(upload_to="songs/", blank=True)

    def __str__(self):
        return f"{self.titulo} from {self.album.titulo}"