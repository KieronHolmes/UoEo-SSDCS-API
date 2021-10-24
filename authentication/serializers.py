""" Serializer class for user registration """
# imports required libraries
import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class RegisterSerializer(ModelSerializer):
    """ Class that validates and creates users using the CustomUser model """

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser

        fields = ("username", "password", "email", "role")
        extra_kwargs = {"email": {"required": True}, "password": {"write_only": True}}

    @staticmethod
    def validate_password(value):
        """ method used to validate password requirements """
        # Password List Source: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials
        # /10k-most-common.txt
        with open("authentication/lists/10k-most-common.txt") as f:
            passwords = {p.strip() for p in f.readlines()}
        # check if the password is in the forbidden list to avoid common passwords
        if value.lower().strip() in passwords:
            raise serializers.ValidationError(
                "You have supplied a commonly used password. Please provide a strong, unique password."
            )
        # using regex to validate minimum password requirements
        if not re.fullmatch(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$",
            value,
        ):
            error_message = "Password does not meet minimum requirements: must be between 8 and 18 characters; "
            error_message += "A mixture of both uppercase and lowercase letters; "
            error_message += "A mixture of letters and number; at least one special character (@$!%*#?&)"
            raise serializers.ValidationError(error_message)
        return value

    @staticmethod
    def validate_role(value):
        """ method to allow valid roles only """
        # list of valid roles. If empty, a Guest user is created.
        valid_roles = ["admin", "researcher", "employee"]
        if value.lower() not in valid_roles:
            raise serializers.ValidationError(
                "Invalid role. Allowed values: Admin / Researcher / Employee"
            )
        return value

    def create(self, validated_data):
        """ if data is validated, create the user calling the objects method of the model """
        user = CustomUser.objects.create_user(**validated_data)
        return user
