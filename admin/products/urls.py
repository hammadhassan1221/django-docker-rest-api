from django.urls import path
from .views import ProductsGenericAPIView
urlpatterns = [
    path('products', ProductsGenericAPIView.as_view()),
    path('products/<str:pk>', ProductsGenericAPIView.as_view())

]