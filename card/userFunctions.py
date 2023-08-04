from rest_framework import status
from rest_framework.response import Response

def createUser(serializer):
    serializer.save()
    responseData=serializer.data.copy()
    return Response(responseData, status=status.HTTP_202_ACCEPTED)

def updateUser(serializer):
    pass

def deleteUser():
    pass