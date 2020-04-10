from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Token
from users.serializers import UserDetailSerializer, TokenSerializer, UserTokenAuthenticationSerializer, UserPasswordAuthenticationSerializer

'''
Used to create/delete a user
'''
class UserDetailView(APIView):
    def post(self, request):
        userDetailSerializer = UserDetailSerializer(data = request.data)
        userDetailSerializer.is_valid(raise_exception = True)

        newUser = userDetailSerializer.save()
        newUser.save()
        newUser.create_update_token()

        return Response(status = status.HTTP_201_CREATED)
    
    def delete(self, request):
        userDetailSerializer = UserDetailSerializer(data = request.data)
        userDetailSerializer.is_valid(raise_exception = True)

        user = userDetailSerializer.save()
        user.delete()

        return Response(status = status.HTTP_200_OK)

'''
To authenticate a user
'''
class UserAuthenticationView(APIView):
    def post(self, request):
        if 'token' in request.data.keys():
            userTokenAuthenticationSerializer = UserTokenAuthenticationSerializer(data = request.data)
            userTokenAuthenticationSerializer.is_valid(raise_exception = True)
            user = userTokenAuthenticationSerializer.create()

            token = Token.objects.get(pk = userTokenAuthenticationSerializer.validated_data['token'].token_string)
            if user.is_token_valid(token):
                return Response(status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_401_UNAUTHORIZED)

        userPasswordAuthenticationSerializer = UserPasswordAuthenticationSerializer(data = request.data)
        userPasswordAuthenticationSerializer.is_valid(raise_exception = True)
        user = userPasswordAuthenticationSerializer.create()
        
        actualUser = User.objects.get(pk = user.email)
        if (user.password == actualUser.password):
            return Response(UserDetailSerializer(actualUser).data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        
