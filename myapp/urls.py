from django.urls import path
from .views import genero_list, home_view, events_view, artists_view, search, profile_view, settings_view, new_artist

urlpatterns = [
    path('generos/', genero_list, name='genero_list'),
    path('', home_view, name='home'),
    path('events/', events_view, name='events'),
    path('artists/', artists_view, name='artists'),
    path('artists/new/', new_artist, name='new_artist'),
    path('profile/', profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),
    path('search/', search, name='search'), 

]
