from re import I
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfully registered new user"
        data['username'] = account.user
    else:
        return Response({'Error'})
