from django import forms
from .models import Artista

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'foto', 'descripcion']

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
        if descripcion and len(descripcion) > 500:
            raise forms.ValidationError("La descripción no puede tener más de 500 caracteres.")
        return descripcion
