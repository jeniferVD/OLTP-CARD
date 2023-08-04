import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Card, Account
from .serializer import UserSerializer, CardSerializer, AccountSerializer
from .userFunctions import getUserById


class UserViewset(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer = self.serializer_class()
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)

    def retrive(self, request, pk=None):
        try:
            return Response(getUserById(pk), status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
