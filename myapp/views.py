from django.shortcuts import render
from .models import GeneroMusical

def genero_list(request):
    generos = GeneroMusical.objects.all()  # Fetch all music genres
    return render(request, 'genero_list.html', {'generos': generos})