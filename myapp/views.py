from django.shortcuts import render, redirect
from .models import Artista
from .forms import ArtistaForm
from django.contrib.auth.decorators import login_required


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

]

def genero_list(request):
    return render(request, 'genero_list.html', {'generos': generos})

def home_view(request):

    return render(request, 'landing_page.html',{"artists": artists})

def events_view(request):
    return render(request, 'events.html')

def artists_view(request):
    return render(request, 'artist/artistas.html')


@login_required
def new_artist(request):
    # Get the artist record for the logged-in user or create a new one
    artista, created = Artista.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artist-profile')  # Replace with the actual URL name for the artist profile
    else:
        form = ArtistaForm(instance=artista)

    return render(request, 'artist/form.html', {'form': form})


def profile_view(request):
    return render(request, 'profile.html')

def settings_view(request):
    return render(request, 'landing_page.html')

def search(request):
    return render(request, 'landing_page.html')

    
