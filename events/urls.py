from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>', views.event_detail, name='event_detail'),
    path('new/', views.create_event, name='event_form'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('add_to_cart/<int:evento_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/<int:evento_id>', views.checkout, name='checkout'),
]