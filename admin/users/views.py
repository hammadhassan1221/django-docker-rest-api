from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

# Create your views here.


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    return Response(users)
