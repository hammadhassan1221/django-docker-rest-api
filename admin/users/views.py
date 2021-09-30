from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView

from .authentication import generate_access_token, JWTAuthentication
from .models import User
from .serializers import UserSerializer


# Create your views here.


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response


#  done this Get authenticated user API work with class and url is : api/user and command is get


class AuthenticatedUser(APIView):
    #  JWT Authentication class made in authentication.py and declared below
    authentication_classes = [JWTAuthentication]
    # By default class to check if user is authenticated
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({
            'data': serializer.data
        })


@api_view(['POST'])
def logout(_):  # use fo under score as we are not using request or any other variable
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'success'
    }

    return response

@api_view(['GET'])
def get_users(request):
    #  ==== Added many = True as list of users is returning
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)
