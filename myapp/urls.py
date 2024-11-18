from django.urls import path
from . import views

urlpatterns = [
    path('generos/', views.genero_list, name='genero_list'),  # URL for listing genres
]
