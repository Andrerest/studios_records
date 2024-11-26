from django import forms
from django.core.exceptions import ValidationError
from .models import Evento, Registracion, Ubicacion, CategoriaEvento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion', 'capacidad', 'precio_entrada']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'nombre': 'Nombre del Evento',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha y Hora de Inicio',
            'fecha_fin': 'Fecha y Hora de Fin',
            'ubicacion': 'Ubicación',
            'capacidad': 'Capacidad Máxima',
            'precio_entrada': 'Precio de Entrada',
        }

    def clean_precio_entrada(self):
        precio_entrada = self.cleaned_data.get('precio_entrada')

        if precio_entrada is not None and precio_entrada < 0:
            raise ValidationError("El precio de entrada no puede ser negativo.")
        
        return precio_entrada

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_fin and fecha_inicio and fecha_fin < fecha_inicio:
            raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")
        
        return cleaned_data
        
# Formulario para registrarse en un evento
class RegistracionForm(forms.ModelForm):
    class Meta:
        model = Registracion
        fields = ['evento', 'usuario', 'estado']
        labels = {
            'evento': 'Evento',
            'usuario': 'Usuario',
            'estado': 'Estado de la Registración',
        }

    def clean(self):
        cleaned_data = super().clean()
        evento = cleaned_data.get('evento')
        usuario = cleaned_data.get('usuario')

        # Validar que el evento no haya alcanzado su capacidad
        if evento and usuario and evento.registraciones.count() >= evento.capacidad:
            raise ValidationError(f"El evento '{evento.nombre}' ha alcanzado su capacidad máxima.")

        # Validar que el usuario no esté ya registrado para el mismo evento
        if evento and usuario and Registracion.objects.filter(evento=evento, usuario=usuario).exists():
            raise ValidationError(f"El usuario {usuario.username} ya está registrado para este evento.")

        return cleaned_data


# Formulario para agregar o actualizar ubicaciones
class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'direccion', 'ciudad', 'pais']
        labels = {
            'nombre': 'Nombre del Lugar',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'pais': 'País',
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        ciudad = cleaned_data.get('ciudad')

        # Validar que no existan ubicaciones duplicadas con el mismo nombre en la misma ciudad
        if Ubicacion.objects.filter(nombre=nombre, ciudad=ciudad).exists():
            raise ValidationError(f"Ya existe una ubicación llamada '{nombre}' en la ciudad '{ciudad}'.")

        return cleaned_data


# Formulario para agregar o actualizar categorías de eventos
class CategoriaEventoForm(forms.ModelForm):
    class Meta:
        model = CategoriaEvento
        fields = ['nombre', 'descripcion', 'eventos']
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
            'eventos': 'Eventos Asociados',
        }
        widgets = {
            'eventos': forms.CheckboxSelectMultiple(),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        # Validar que el nombre de la categoría sea único
        if CategoriaEvento.objects.filter(nombre=nombre).exists():
            raise ValidationError(f"Ya existe una categoría con el nombre '{nombre}'.")

        return nombre
