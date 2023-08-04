import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializer import UserSerializer
from .api import createUser

class UserViewset(viewsets.ViewSet):
    qryset=User.objects.all()
    serializer_class= UserSerializer

    def create(self, request):
        try:
            return createUser(request)
        except Exception as err:
            return Response(
                {'message':f'Server Error: {err}' },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )