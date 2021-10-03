from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from admin.pagination import CustomPagination
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer
from users.authentication import JWTAuthentication


class OrderGenericAPIView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk)
            })
        return self.list(request)

