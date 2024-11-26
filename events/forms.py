from django import forms
from django.core.exceptions import ValidationError
from .models import Evento
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
