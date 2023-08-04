import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Card, Account, Transaction
from .serializer import UserSerializer, CardSerializer, AccountSerializer, TransactionSerializer
from .userFunctions import getUserById
from django.shortcuts import get_object_or_404


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewset(viewsets.ViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        cardNumber = request.data.get("card")
        amountSpent = request.data.get("amountSpent")
        card = Card.objects.filter(cardNumber=cardNumber).values()
        if not card:
            return Response('Invalid Card', status=status.HTTP_404_NOT_FOUND)
        card = card[0]
                
        account = Account.objects.filter(pk=card.get('accountID_id')).values()[0]        
        if amountSpent >= account.get('balance'):
            return Response('Insufficient funds', status=status.HTTP_400_BAD_REQUEST)
        
        Transaction.objects.create(cardID = Card.objects.filter(pk=card.get('id'))[0], amountSpent = amountSpent)
        newbalance = account.get('balance') - amountSpent
        Account.objects.filter(pk=account.get('id')).update(balance=newbalance)
        
        return Response('Ok', status=status.HTTP_201_CREATED)
        