from django.urls import path
from .views import genero_list, home_view, events_view, artists_view, search

urlpatterns = [
    path('generos/', genero_list, name='genero_list'),
    path('', home_view, name='home'),
    path('events/', events_view, name='events'),
    path('artists/', artists_view, name='artists'),
    path('search/', search, name='search'), 
]
