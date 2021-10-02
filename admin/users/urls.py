from django.urls import path
from .views import (
    get_users,
    register,
    login,
    AuthenticatedUser,
    logout,
    PermissionAPIView,
    RoleViewSet,
    UserGenericAPIView
)

urlpatterns = [
    path('users', get_users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path('permission', PermissionAPIView.as_view()),

    # Role view sets
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        }
    )),

    # Generic views implementation for users related APIs
    path('generic_view/users', UserGenericAPIView.as_view()),
    path('generic_view/users/<str:pk>', UserGenericAPIView.as_view())

]
