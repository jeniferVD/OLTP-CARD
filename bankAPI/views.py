import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Card, Account
from .serializer import UserSerializer, CardSerializer, AccountSerializer
from .userFunctions import getUserById
from django.shortcuts import get_object_or_404


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
