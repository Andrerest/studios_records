from django.urls import path, include
from .views import login_view, register_view, logout_view, test_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'), 
    path('test/', test_view, name='test')
    ]
    