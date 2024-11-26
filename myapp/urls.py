from django.urls import path, include
from .views import genero_list, home_view, events_view, search, profile_view, settings_view

urlpatterns = [
    path('generos/', genero_list, name='genero_list'),
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),
    path('search/', search, name='search'), 
    path('events/', include('events.urls'), name='events'),
    path('artists/', include('artist.urls'), name='artists'),
]
