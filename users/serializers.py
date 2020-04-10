from rest_framework import serializers
from users.models import User, Token

class UserPasswordAuthenticationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)

    class Meta():
        model = User
        fields = ['email', 'password']

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data
        return User(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['email', 'name', 'password', 'token']

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data

        return User(**validated_data)

class TokenSerializer(serializers.ModelSerializer):
    class Meta():
        model = Token
        fields = ['user']

class UserTokenAuthenticationSerializer(serializers.Serializer):
    token = serializers.SlugRelatedField(slug_field = 'token_string', queryset = Token.objects.all())
    email = serializers.SlugRelatedField(slug_field = 'email', queryset = User.objects.all())

    def create(self):
        user_email = self.validated_data['email']
        user = User.objects.get(pk = user_email.email)

        return user
