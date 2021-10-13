from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class RegisterSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'email': {'required': True}
        }

    def validate_password(self, value):
        # Password List Source: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
        with open('authentication/lists/10k-most-common.txt') as f:
            passwords = {p.strip() for p in f.readlines()}

        if value.lower().strip() in passwords:
            raise serializers.ValidationError("You have supplied a commonly used password. Please provide a strong, unique password.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

        return user
