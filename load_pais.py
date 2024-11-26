# load_paises.py

from locations.models import Pais

# Lista de países que deseas cargar
paises = [
    "Argentina", "Brasil", "Canada", "Chile", "Colombia", "Espana", "Francia",
    "Alemania", "Italia", "Mexico", "Peru", "Reino Unido", "Estados Unidos",
    "Uruguay", "Venezuela", "Australia", "Japon", "China", "India", "Rusia",
    "Sudafrica", "Nigeria", "Egipto", "Arabia Saudita", "Turquia", "Corea del Sur",
    "Nueva Zelanda", "Suecia", "Noruega", "Paises Bajos"
]

# Guardar los países en la base de datos
for pais in paises:
    if not Pais.objects.filter(nombre=pais).exists():
        Pais.objects.create(nombre=pais)
        print(f'País "{pais}" guardado correctamente.')
    else:
        print(f'El país "{pais}" ya existe.')
