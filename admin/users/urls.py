from django.urls import path
from .views import get_users, register, login, AuthenticatedUser, logout, PermissionAPIView

urlpatterns = [
    path('users', get_users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path('permission', PermissionAPIView.as_view())
]
