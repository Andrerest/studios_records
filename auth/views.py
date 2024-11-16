from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/index.html')

def profile(request):
    return render(request, 'pages/profile.html')

def notification(request):
    return render(request, 'pages/notification.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home/')  
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


##


def register(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/auth-signup.html', {'form': form})






def password_reset(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/auth-reset.html', {'form': form})