from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from artist.models import Artista
from .models import Evento
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from decimal import Decimal

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

def add_to_cart(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    # Get ticket type and quantity from POST request
    ticket_type = request.POST.get('ticketType')
    try:
        ticket_quantity = int(request.POST.get('ticketQuantity', 0))
    except ValueError:
        ticket_quantity = 0  # Ensure a valid integer if it's not present or invalid

    # Initialize or get the cart from the session
    cart = request.session.get('cart', [])

    # Get ticket price and convert it to float
    ticket_price = float(evento.entrada_general) if ticket_type == 'general' else float(evento.entrada_vip)

    # Add the selected ticket to the cart
    cart.append({
        'evento_id': evento.id,
        'evento_name': evento.nombre,
        'ticket_type': ticket_type,
        'ticket_quantity': ticket_quantity,
        'ticket_price': ticket_price,  # Store price as float
    })

    # Save the updated cart in the session
    request.session['cart'] = cart

    # Redirect to the cart page
    return redirect('events:cart')


def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])
    
    # Calculate the total amount, ensuring prices are floats
    total = sum(item['ticket_price'] * item['ticket_quantity'] for item in cart)

    # Ensure the total is a float
    total = float(total)

    # Render the checkout page with cart and total context
    return render(request, 'event/checkout.html', {
        'cart': cart,
        'total': total,
    })


@login_required
def checkout(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])
    
    if request.method == 'POST':
        # Process the checkout
        for item in cart:
            evento = get_object_or_404(Evento, id=item['evento_id'])
            
            # Check for sufficient ticket quantity
            if item['ticket_type'] == 'general' and item['ticket_quantity'] <= evento.cantidad_general:
                evento.cantidad_general -= item['ticket_quantity']
            elif item['ticket_type'] == 'vip' and item['ticket_quantity'] <= evento.cantidad_vip:
                evento.cantidad_vip -= item['ticket_quantity']
            else:
                # If not enough tickets, redirect to an error page
                return redirect('error_page')  # Or show a custom error message in the template

            evento.save()  # Save the updated event data

            # Save the transaction
            total_amount = Decimal(item['ticket_price']) * item['ticket_quantity']
            transaction = Transaction.objects.create(
                user=request.user,
                evento=evento,
                ticket_type=item['ticket_type'],
                ticket_quantity=item['ticket_quantity'],
                ticket_price=Decimal(item['ticket_price']),
                total_amount=total_amount,
                status='completed',  # Update status to 'completed' after processing payment
            )
            transaction.save()

        # Here, you can add the logic to handle payment processing (e.g., via a payment gateway)

        # Clear the cart from the session after checkout
        request.session['cart'] = []

        # Redirect to a confirmation page
        return redirect('events:order_confirmation')  # Assuming you have a confirmation page

    # If the method is GET, render the checkout page with cart and total
    total = sum(item['ticket_price'] * item['ticket_quantity'] for item in cart)
    return render(request, 'event/checkout.html', {
        'cart': cart,
        'total': total,
    })