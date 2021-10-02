from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from admin.pagination import CustomPagination
from .models import Product
from .serializers import ProductSerializer
from users.authentication import  JWTAuthentication


class ProductsGenericAPIView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk)
            })
        return self.list(request)

    def post(self, request):
        return Response({
            'data': self.create(request).data
        })

    def put(self, request, pk=None):

        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
