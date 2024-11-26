from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista
from .forms import ArtistaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def artist_list(request):
    all_artists = Artista.objects.all()
    """
    sorted_artists = sorted(all_artists, key=lambda artista: artista.total_seguidores(), reverse=True)
    top_artists = sorted_artists[:] 
    """

    top_artists_data = [
        {
            "image_url": artist.foto.url if artist.foto else "static\images\default_profile_image.png",
            "name": artist.nombre,
            "description": artist.descripcion,
            "followers_count": artist.total_seguidores(),
            "username": artist.user.username,
        }
        for artist in all_artists
    ]
    return render(request, 'artist/list.html', {'top_artists': top_artists_data})

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
    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES)
        print("Form: ", form.data)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()
            return redirect('artist_list')
            #return redirect('artist_detail', pk=artist.pk)  # Adjust the redirect
        else:
            print(form.errors)
    else:
        
        form = ArtistaForm()
    return render(request, 'artist/form.html', {'form': form})