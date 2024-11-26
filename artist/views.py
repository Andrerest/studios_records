from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista
from .forms import ArtistaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def artist_list(request):
    artista = None
    if request.user.is_authenticated:
        artista = Artista.objects.filter(user=request.user).first()


    all_artists = Artista.objects.all()
    top_artists_data = [
        {
            "image_url": artist.foto.url if artist.foto else "media\artistas\default_profile_image.png",
            "name": artist.nombre,
            "description": artist.descripcion,
            "followers_count": artist.total_seguidores(),
            "username": artist.user.username,
        }
        for artist in all_artists
    ]

    return render(request, 'artist/list.html', {'artista': artista,'top_artists': top_artists_data})

def artist_detail(request, artist_username):
    artist = get_object_or_404(Artista, user__username=artist_username)
        # Fetch upcoming events and featured tracks (this assumes you have Event and Track models)
    #upcoming_events = Event.objects.filter(artist=artist).order_by('event_date')
    #featured_tracks = Track.objects.filter(artist=artist, is_featured=True)

    return render(request, 'artist/details.html', {
        'artist': artist,
        #'upcoming_events': upcoming_events,
        #'featured_tracks': featured_tracks
    })


def follow_artist(request, artist_id):
    artista = get_object_or_404(Artista, id=artist_id)
    if request.user.is_authenticated:
        if request.user in artista.seguidores.all():
            artista.seguidores.remove(request.user)
        else:
            artista.seguidores.add(request.user)
    return redirect('artist_detail', artist_id=artist_id)

@login_required
def create_artist(request):
    artist = Artista.objects.filter(user=request.user).first()

    if request.method == "POST":
        # Bind the form data and files to the existing artist or create a new one
        form = ArtistaForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user  # Ensure the user is always set to the logged-in user
            artist.save()
            return redirect('artists:artist_list')  # Redirect to the artist list or another page
        else:
            print(form.errors)
    else:
        # Prepopulate the form with the artist's instance if it exists
        form = ArtistaForm(instance=artist)

    return render(request, 'artist/form.html', {'form': form})