from django.contrib import admin
from .models import Artista, Album, Cancion

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'user', 'total_seguidores')
    search_fields = ('nombre', 'nacionalidad')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'fecha_lanzamiento')
    list_filter = ('fecha_lanzamiento',)

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracion')