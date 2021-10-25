"""
File to handle Django serialization of the Register functionality.
"""
import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class RegisterSerializer(ModelSerializer):
    """
    Class that serializes, validates and creates users using the CustomUser model.
    """

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        """
        Specifies the model to be used for the serializer, the fields available and any other attribute modifiers to be used.s
        """

        model = CustomUser

        fields = ("username", "password", "email", "role")
        extra_kwargs = {"email": {"required": True}, "password": {"write_only": True}}

    @staticmethod
    def validate_password(value):
        """
        Validates whether the supplied input meets the applications minimum security requirements.
        Password must not be in the 10k most commonly used passwords (Available from: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt)
        and must contain 8-18 characters including a mixture of upper and lower case characters, with one special character (@$!%*#?&).
        """
        with open("authentication/lists/10k-most-common.txt") as f:
            passwords = {p.strip() for p in f.readlines()}
        # check if the password is in the forbidden list to avoid common passwords
        if value.lower().strip() in passwords:
            raise serializers.ValidationError(
                "You have supplied a commonly used password. Please provide a strong, unique password."
            )
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
        """
        Validates whether the requested role is valid.
        Admin/Researcher/Employee are the options which can be requested from the Registration endpoint.
        """
        # list of valid roles. If empty, a Guest user is created.
        valid_roles = ["admin", "researcher", "employee"]
        if value.lower() not in valid_roles:
            raise serializers.ValidationError(
                "Invalid role. Allowed values: Admin / Researcher / Employee"
            )
        return value

    def create(self, validated_data):
        """
        If the validation stages have been completed, the user is to be created with the supplied information.
        """
        user = CustomUser.objects.create_user(**validated_data)
        return user
