from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer, UserAuthenticationSerializer

'''
Used to create a user
'''
class UserDetailView(APIView):
    def post(self, request):
        userSerializer = UserSerializer(data = request.data)
        if (userSerializer.is_valid(raise_exception = True)):
            savedUser = userSerializer.save()
            return Response(status = status.HTTP_201_CREATED)
            

'''
To authenticate a user
'''
class UserAuthenticationView(APIView):
    def post(self, request):
        userAuthenticationSerializer = UserAuthenticationSerializer(data = request.data)
        if (userAuthenticationSerializer.is_valid(raise_exception = True)):
            # TODO: Update the token
            return Response(status = status.HTTP_200_OK)
