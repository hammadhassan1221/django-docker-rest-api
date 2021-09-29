from django.urls import path
from users.views import hello

urlpatterns = [
    path('hello', hello),
]
