from django.db import models

class User(models.Model):
    name = models.TextField(null=True)
    lastName = models.TextField(null=True)
    address = models.TextField(null=True)
    phoneNumber = models.TextField(null=True)
    email = models.TextField(null=True)
    genre = models.CharField(max_length=1, null=True)  # F=Female or M=Male


class Account(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    accountNumber = models.IntegerField(null=True)
    accountType = models.CharField(max_length=1, null=True)  # D = Debit, C = Credit
    balance = models.FloatField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    idUser = models.IntegerField("bankAPI.User")


class Card(models.Model):
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE, null=True) 
    cardNumber = models.IntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    holder = models.TextField(null=True)
    idAccount = models.IntegerField(
        "bankAPI.Account"
    )
