from django import forms
from django.core.exceptions import ValidationError
from .models import Evento, Registracion
import datetime
# Formulario para crear un Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'foto', 'descripcion', 'fecha_inicio', 'fecha_fin', 'direccion', 'ciudad', 'pais', 'entrada_general', 'entrada_vip', 'cantidad_general', 'cantidad_vip']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Evento'}),
            'foto': forms.ClearableFileInput(attrs={ 'class': 'form-control-file' }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Evento'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'entrada_general': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio General', 'step': '100'}),
            'entrada_vip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio VIP' , 'step': '100'}),
            'cantidad_general': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de Entradas Generales', 'step': '1'}),
            'cantidad_vip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de Entradas VIP' , 'step': '1'}),
        }
        labels = {
            'nombre': 'Nombre del Evento',
            'foto': 'Foto',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha y Hora de Inicio',
            'fecha_fin': 'Fecha y Hora de Fin',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'pais': 'País',
            'entrada_general': 'Precio General',
            'entrada_vip': 'Precio VIP',
            'cantidad_general': 'Cantidad de Entradas Generales',
            'cantidad_vip': 'Cantidad de Entradas VIP',
        }


    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio < datetime.date.today():
            raise ValidationError("La fecha de inicio no puede ser anterior a la fecha actual.")
        return fecha_inicio
    
    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')
        if fecha_fin < self.cleaned_data.get('fecha_inicio'):
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")
        return fecha_fin

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            # If no photo is provided, return None, and the default image will be used
            return None
            
        if foto:
            # Check if the file is a valid image
            if not foto.content_type.startswith('image'):
                raise forms.ValidationError("Por favor, suba un archivo de imagen válido.")
            # Optional: Check file size (limit to 5MB for example)
            if foto.size > 5 * 1024 * 1024:  # 5 MB limit
                raise forms.ValidationError("La imagen no debe exceder los 5MB.")
        return foto

# Formulario para registrarse en un evento
class RegistracionForm(forms.ModelForm):
    tipo_entrada = forms.ChoiceField(
        choices=[("general", "General"), ("vip", "VIP")],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo de Entrada'
    )

    class Meta:
        model = Registracion
        fields = ['evento', 'usuario', 'tipo_entrada', 'estado']
        labels = {
            'evento': 'Evento',
            'usuario': 'Usuario',
            'estado': 'Estado de la Registración',
            'tipo_entrada': 'Tipo de Entrada',
        }

    def clean(self):
        cleaned_data = super().clean()
        evento = cleaned_data.get('evento')
        usuario = cleaned_data.get('usuario')
        tipo_entrada = cleaned_data.get('tipo_entrada')

        # Validar que el evento no haya alcanzado su capacidad para el tipo de entrada
        if evento:
            if tipo_entrada == "general" and evento.registraciones.filter(tipo_entrada="general").count() >= evento.cantidad_general:
                raise ValidationError(f"El evento '{evento.nombre}' ha alcanzado la capacidad máxima para entradas generales.")
            elif tipo_entrada == "vip" and evento.registraciones.filter(tipo_entrada="vip").count() >= evento.cantidad_vip:
                raise ValidationError(f"El evento '{evento.nombre}' ha alcanzado la capacidad máxima para entradas VIP.")
        
        # Validar que el usuario no esté ya registrado para el mismo evento con el mismo tipo de entrada
        if evento and usuario and Registracion.objects.filter(evento=evento, usuario=usuario, tipo_entrada=tipo_entrada).exists():
            raise ValidationError(f"El usuario {usuario.username} ya está registrado para este evento con tipo de entrada {tipo_entrada}.")

        return cleaned_data
