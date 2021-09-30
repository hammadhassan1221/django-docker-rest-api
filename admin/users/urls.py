from django.urls import path
from .views import get_users, register, login, AuthenticatedUser

urlpatterns = [
    path('users', get_users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view())
]
