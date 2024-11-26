from django import forms
from .models import Artista
from django.contrib.auth.models import User

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        
        fields = ['nombre','correo', 'foto', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del artista'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el correo electrónico del artista'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una descripción',
                'rows': 4
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'foto': 'Foto',
            'descripcion': 'Descripción',

        }
        help_texts = {
            'nombre': 'El nombre debe tener entre 3 y 100 caracteres.',
            'correo': 'El correo electrónico debe de ser válido',
            'foto': 'Suba una imagen válida, de un tamaño máximo de 5MB.',
            'descripcion': 'Máximo 500 caracteres permitidos.',
        }

    # Custom validation for 'nombre'
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre no puede tener más de 100 caracteres.")
        return nombre

    # Custom validation for 'foto' (if needed)
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

    # Custom validation for 'descripcion' (optional)
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) > 300:
            raise forms.ValidationError("La descripción no puede tener más de 300 caracteres.")
        return descripcion

    def save(self, commit=True, user=None):
            # Save Artista instance
            artista = super().save(commit=False)
            if user:  # Link the Artista instance with the authenticated user
                artista.user = user
            if commit:
                artista.save()
            
            # Update user information
            if user:
                user.email = self.cleaned_data['email']
                user.save()
            
            return artista