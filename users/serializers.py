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

        return User.objects.get(pk = validated_data['email'])

class UserRetrievalSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)

    class Meta():
        model = User
        fields = ['email']

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data

        return User.objects.get(pk = validated_data['email'])

class UserDetailSerializer(serializers.ModelSerializer):
    token = serializers.PrimaryKeyRelatedField(queryset=Token.objects.all(), required = False)

    class Meta():
        model = User
        fields = ['email', 'name', 'password', 'token']

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data

        return User(**validated_data)

class TokenSerializer(serializers.ModelSerializer):
    token_string = serializers.CharField(max_length=100)

    class Meta():
        model = Token
        fields = ['token_string']

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data

        return Token.objects.get(pk = validated_data['token_string'])
