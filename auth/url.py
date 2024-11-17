from django.urls import path, include
from .views import login_view, register_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
    ]
    