from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # The user is authenticated
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Iniciaste sesión correctamente!')
            return redirect('home')  # Redirect to home after successful login
        else:
            # Form is invalid, display errors
            messages.error(request, 'Credenciales incorrectas. Por favor intenta de nuevo.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})  


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            # If form is not valid, pass the form errors to the context (no need to use messages here)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def test_view(request):
    return render(request, 'test.html')