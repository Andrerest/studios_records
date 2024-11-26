from django.shortcuts import render, redirect
from .forms import EventoForm

def event_list(request):
    return render(request, 'event/list.html')

def create_event(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventoForm()
    return render(request, 'event/form.html', {'form': form})