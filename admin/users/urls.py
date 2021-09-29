from django.urls import path
from .views import get_users, register

urlpatterns = [
    path('users', get_users),
    path('register', register),
]
