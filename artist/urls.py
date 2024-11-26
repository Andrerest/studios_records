from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('new/', views.create_artist, name='artist_form'),
    path('<str:artist_username>/', views.artist_detail, name='artist_detail'),
    path('<int:artist_username>/follow/', views.follow_artist, name='follow_artist'),
]
