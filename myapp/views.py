from django.shortcuts import render
from .models import GeneroMusical

def genero_list(request):
    generos = GeneroMusical.objects.all()  # Fetch all music genres
    return render(request, 'genero_list.html', {'generos': generos})
    

def home_view(request):
    
    
    return render(request, 'landing_page.html',{"artists": artists})
artists = [
    {
        "name": "Deadmau5",
        "description": "DJ y productor canadiense de música electrónica, famoso por su casco de ratón y éxitos como 'Strobe.'",
        "image_url": "https://www.billboard.com/wp-content/uploads/media/14-deadmau5-ultra-2014-650.jpg?w=650&h=430&crop=1",
        "ticket_url": "test.html",
    },
    {
        "name": "Skrillex",
        "description": "Productor estadounidense y figura clave del dubstep, conocido por 'Bangarang' y su estilo innovador.",
        "image_url": "https://www.billboard.com/wp-content/uploads/media/skrillex-with-jack-u-perform-weekend-2-coachella-2016-billboard-650.jpg?w=650&h=430&crop=1",
        "ticket_url": "test.html",
    },
    {
        "name": "Bad Bunny",
        "description": "Cantante puertorriqueño de reguetón y trap latino, con éxitos globales como 'Tití Me Preguntó.'",
        "image_url": "https://www.billboard.com/wp-content/uploads/2020/12/Bad-Bunny-2-credit-STILLZ-bb19-2020-billlboard-1548-1608056785.jpg?w=942&h=623&crop=1",
        "ticket_url": "test.html",
    },
        {
        "name": "Avicii",
        "description": "DJ y productor sueco conocido por éxitos como 'Wake Me Up' y 'Levels', influyente en la música electrónica moderna.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Avicii_2014_002.jpg",
        "ticket_url": "avicii.html"
    },
    {
        "name": "Daft Punk",
        "description": "Dúo francés de música electrónica que combina house, funk y disco. Famosos por sus cascos robóticos y éxitos como 'Get Lucky.'",
        "image_url": "https://media.pitchfork.com/photos/5929af605c3a2459a49ef3a3/1:1/w_600/4e2c4e18.jpg",
        "ticket_url": "daftpunk.html"
    },
    {
        "name": "Armin van Buuren",
        "description": "DJ y productor neerlandés, conocido como uno de los principales nombres del trance, con éxitos como 'This Is What It Feels Like.'",
        "image_url": "https://www.billboard.com/wp-content/uploads/media/01-armin-van-buuren-press-photo-2014-650.jpg",
        "ticket_url": "armin.html"
    },
    ]    

def events_view(request):
    return render(request, 'events.html')

def artists_view(request):
    return render(request, 'artista.html',{"artists": artists})

def profile_view(request):
    return render(request, 'landing_page.html')

def settings_view(request):
    return render(request, 'landing_page.html')

def search(request):
    return render(request, 'landing_page.html')

    