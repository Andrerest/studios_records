from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('new/', views.create_event, name='event_form'),
    path('<str:event_id>/', views.event_list, name='artist_detail'),
    path('<int:event_id>/follow/', views.event_list, name='follow_artist'),
]
