from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>', views.event_detail, name='event_detail'),
    path('new/', views.create_event, name='event_form'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),

    path('buy-ticket/', views.buy_ticket, name='buy_ticket'),
]