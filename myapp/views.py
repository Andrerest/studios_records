from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def genero_list(request):
    return render(request, 'genero_list.html')

def home_view(request):

    return render(request, 'test.html')

def events_view(request):
    return render(request, 'events.html')





def profile_view(request):
    return render(request, 'profile/details.html')

def settings_view(request):
    return render(request, 'landing_page.html')

def search(request):
    return render(request, 'landing_page.html')

    
