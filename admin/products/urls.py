from django.urls import path
from .views import ProductsGenericAPIView, FileUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products', ProductsGenericAPIView.as_view()),
    path('products/<str:pk>', ProductsGenericAPIView.as_view()),
    path('upload', FileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)