import os
from rest_framework import status
from rest_framework.response import Response
from .models import User, Account, Card


def createUser(request):
    data = request.data
