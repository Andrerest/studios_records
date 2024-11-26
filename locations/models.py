from django.db import models

# Create Pais model
class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Países"

# Create Ciudad model
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, related_name='ciudades', on_delete=models.CASCADE)  # Link Ciudad to Pais
    def __str__(self):
        return f"{self.nombre}, {self.pais.nombre}"

    class Meta:
        verbose_name_plural = "Ciudades"