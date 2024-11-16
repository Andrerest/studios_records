from django.urls import path, include
from .views import login, register, password_reset

urlpatterns = [
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/password-reset/', password_reset, name='password_reset'),
    path('', login, name='login'),
    
    ]
    