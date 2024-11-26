from locations.models import Pais, Ciudad

# Diccionario con países y ciudades
ciudades = {
    "Argentina": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata"],
    "Brasil": ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador", "Porto Alegre"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Ottawa", "Calgary"],
    "Chile": ["Santiago", "Valparaiso", "Concepcion", "La Serena", "Antofagasta"],
    "Colombia": ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena"],
    "Espana": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"],
    "Francia": ["Paris", "Marsella", "Lyon", "Toulouse", "Niza"],
    "Alemania": ["Berlin", "Munich", "Hamburgo", "Frankfurt", "Colonia"],
    "Italia": ["Roma", "Milano", "Napoli", "Torino", "Florencia"],
    "Mexico": ["Ciudad de Mexico", "Guadalajara", "Monterrey", "Cancun", "Puebla"],
    "Peru": ["Lima", "Arequipa", "Cusco", "Trujillo", "Chiclayo"],
    "Reino Unido": ["Londres", "Manchester", "Edimburgo", "Birmingham", "Glasgow"],
    "Estados Unidos": ["Nueva York", "Los Angeles", "Chicago", "Miami", "San Francisco"],
    "Uruguay": ["Montevideo", "Punta del Este", "Salto", "Paysandu", "Colonia del Sacramento"],
    "Venezuela": ["Caracas", "Maracaibo", "Valencia", "Barquisimeto", "Ciudad Guayana"],
    "Australia": ["Sidney", "Melbourne", "Brisbane", "Perth", "Adelaida"],
    "Japon": ["Tokio", "Osaka", "Kioto", "Yokohama", "Sapporo"],
    "China": ["Beijing", "Shanghai", "Hong Kong", "Shenzhen", "Guangzhou"],
    "India": ["Nueva Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai"],
    "Rusia": ["Moscu", "San Petersburgo", "Novosibirsk", "Yekaterinburgo", "Nizhni Novgorod"],
    "Sudafrica": ["Johannesburgo", "Ciudad del Cabo", "Durban", "Pretoria", "Port Elizabeth"],
    "Nigeria": ["Lagos", "Abuja", "Kano", "Ibadan", "Port Harcourt"],
    "Egipto": ["El Cairo", "Alejandria", "Giza", "Sharm el-Sheikh", "Luxor"],
    "Arabia Saudita": ["Riad", "Yeda", "La Meca", "Medina", "Dammam"],
    "Turquia": ["Estambul", "Ankara", "Izmir", "Antalya", "Bursa"],
    "Corea del Sur": ["Seul", "Busan", "Incheon", "Daegu", "Gwangju"],
    "Nueva Zelanda": ["Auckland", "Wellington", "Christchurch", "Hamilton", "Dunedin"],
    "Suecia": ["Estocolmo", "Gotemburgo", "Malmo", "Uppsala", "Vasteras"],
    "Noruega": ["Oslo", "Bergen", "Stavanger", "Trondheim", "Drammen"],
    "Paises Bajos": ["Amsterdam", "Rotterdam", "La Haya", "Utrecht", "Eindhoven"]
}

def cargar_ciudades():
    for pais_nombre, ciudades_lista in ciudades.items():
        # Obtener el pais por nombre o crear si no existe
        pais, creado = Pais.objects.get_or_create(nombre=pais_nombre)
        
        # Para cada ciudad, crearla asociada al país
        for ciudad_nombre in ciudades_lista:
            # Crear la ciudad asociada al país
            Ciudad.objects.get_or_create(nombre=ciudad_nombre, pais=pais)
    
    print("Ciudades cargadas exitosamente.")

# Llamar a la función para cargar las ciudades
if __name__ == "__main__":
    cargar_ciudades()
