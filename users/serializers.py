from rest_framework import serializers
from users.models import User, Token

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['email', 'name', 'password']

class TokenSerializer(serializers.ModelSerializer):
    class Meta():
        model = Token
        fields = ['user']

# A few ways to do this
# First is to create a class that contains a User and a Token and create a serializer for that
# Problems that exist here are that the TokenSerializer cannot be created with a Token object in which email is a duplicate. I don't want to have this validation for TokenSerializer
# Second is to create a serializer that contains a UserSerializer and a TokenSerializer, UserAuthenticationSerializer
# Third is to extract the user part and the token part in the view itself and use UserSerializer and TokenSerializer independently.

# How would password and token work as well? Single serializer UserAuthenticationSerializer would be correct

class UserAuthenticationSerializer(serializers.Serializer):
    userSerializer = UserSerializer()
    tokenSerializer = TokenSerializer()

    def validate(self):
        print('validate called')
    
    def create(self, validated_data):
        print('create called')
    #     userData = validated_data.pop('user')
    #     tokenData = validated_data.pop('token')

    #     print(userData)
    #     print(tokenData)
