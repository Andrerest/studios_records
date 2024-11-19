# admin.py
from django.contrib import admin
from .models import Artista

@admin.register(Artista)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')