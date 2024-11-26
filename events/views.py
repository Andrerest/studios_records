from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from artist.models import Artista
from .models import Evento
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def event_list(request):
    artista = None
    if request.user.is_authenticated:
        artista = Artista.objects.filter(user=request.user).first()

    now = timezone.now()
    upcoming_events = Evento.objects.filter(fecha_inicio__gte=now).order_by('fecha_inicio')
    upcoming_events_data = [
        {
            "id": event.id,
            "image_url": event.foto.url if event.foto else None,
            "name": event.nombre,
            "description": event.descripcion,
            "start_date": event.fecha_inicio,
            "end_date": event.fecha_fin,
            "city": event.ciudad,
            "country": event.pais,
            "price": event.entrada_general,
        }
        for event in upcoming_events
    ]
    
    print("Events: ", upcoming_events_data)

    return render(request, 'event/list.html', {
        'artista': artista,
        'upcoming_events': upcoming_events_data
    })

def event_detail(request, event_id):
    event = get_object_or_404(Evento, id=event_id)
        # Fetch upcoming events and featured tracks (this assumes you have Event and Track models)
    #upcoming_events = Event.objects.filter(artist=artist).order_by('event_date')
    #featured_tracks = Track.objects.filter(artist=artist, is_featured=True)

    return render(request, 'event/details.html', {
        'evento': event,
        #'upcoming_events': upcoming_events,
        #'featured_tracks': featured_tracks
    })
        
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        print("Form: ", form.data)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('events:event_list')  # Redirect after successful form submission
    else:
        form = EventoForm()

    return render(request, 'event/form.html', {'form': form})

@login_required
def edit_event(request, id):
    event = get_object_or_404(Evento, id=id)

    if request.method == "POST":
        form =EventoForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')  # Redirect to the artist list or another page
        else:
            print(form.errors)
    else:
        form = EventoForm(instance=event)
        print("Evento: ",form)

    return render(request, 'event/form.html', {'form': form})





def test_evento_form(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        print("Is form valid: ", form.is_valid())
        print("Form data: ", form.cleaned_data)
        if form.is_valid():
    # If form is valid
            print("Form is valid")
        else:
            # If form is invalid
            print("Form is invalid")
            print(form.errors)
    else:
        form = EventoForm()
    return render(request, 'event/test.html', {'form': form})

def buy_ticket(request):
    artista = None
    if request.user.is_authenticated:
        artista = Artista.objects.filter(user=request.user).first()

    return render(request, 'event/buy_ticket.html', {
        'artista': artista,
    })