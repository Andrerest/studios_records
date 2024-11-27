from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'ciudad', 'pais', 'entrada_general', 'entrada_vip', 'cantidad_general', 'cantidad_vip')
    list_filter = ('fecha_inicio', 'ciudad', 'pais')
    search_fields = ('nombre', 'ciudad', 'pais')
    ordering = ('fecha_inicio',)
    readonly_fields = ('cantidad_general', 'cantidad_vip')  # If quantities should not be editable manually

    # Optional: Group related fields into sections
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'descripcion', 'foto', 'direccion', 'ciudad', 'pais', 'fecha_inicio', 'fecha_fin')
        }),
        ('Entradas y Disponibilidad', {
            'fields': ('entrada_general', 'entrada_vip', 'cantidad_general', 'cantidad_vip')
        }),
    )
