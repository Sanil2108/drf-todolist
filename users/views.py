from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Token
from users.serializers import UserDetailSerializer, UserRetrievalSerializer, TokenSerializer, UserPasswordAuthenticationSerializer

'''
Used to create/delete a user
'''
class UserDetailView(APIView):
    def post(self, request):
        userDetailSerializer = UserDetailSerializer(data = request.data)
        userDetailSerializer.is_valid(raise_exception = True)

        newUser = userDetailSerializer.create()
        newUser.create_update_token()
        newUser.save()

        return Response(status = status.HTTP_201_CREATED)
    
    def delete(self, request):
        userPasswordAuthenticationSerializer = UserPasswordAuthenticationSerializer(data = request.data)
        userPasswordAuthenticationSerializer.is_valid(raise_exception = True)

        user = userPasswordAuthenticationSerializer.create()
        user.delete()

        return Response(status = status.HTTP_200_OK)

'''
To authenticate a user using a token
'''
class UserTokenAuthenticationView(APIView):

    def post(self, request):
        if 'user' not in request.data:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        userData = request.data['user']
        userRetrievalSerializer = UserRetrievalSerializer(data = userData)
        userRetrievalSerializer.is_valid(raise_exception = True)
        user = userRetrievalSerializer.create()

        if 'token' not in request.data.keys():
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        tokenData = request.data['token']
        tokenSerializer = TokenSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)
        token = tokenSerializer.create()
        
        if user.is_token_valid(token):
            return Response(status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_401_UNAUTHORIZED)


'''
To authenticate a user using password
'''
class UserPasswordAuthenticationView(APIView):

    def post(self, request):
        if 'user' not in request.data:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        userData = request.data['user']
        userPasswordAuthenticationSerializer = UserPasswordAuthenticationSerializer(data = userData)
        userPasswordAuthenticationSerializer.is_valid(raise_exception = True)
        user = userPasswordAuthenticationSerializer.create()

        userDetailSerializer = UserDetailSerializer(user)

        return Response(userDetailSerializer.data, status = status.HTTP_200_OK)
