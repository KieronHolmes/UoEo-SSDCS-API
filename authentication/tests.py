"""
Tests the User registration functionality.
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser


class RegisterTests(APITestCase):
    """
    Class to group the Registration tests.
    """

    def test_register_valid(self):
        """
        Register a valid user account.
        """
        url = reverse("register_user")
        data = {
            "username": "valid-user",
            "password": "r4Mns&ywn2837",
            "email": "valid.user@example.com",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "valid-user")

    def test_register_invalid(self):
        """
        Attempt to register an invalid user account.
        """
        url = reverse("register_user")
        data = {
            "username": "invalid-user",
            "email": "ThisIsNotAnEmailAddress",
            "password": "r4Mns&ywn2837",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_common_password(self):
        """
        Attempt to register a user account with a commonly used password.
        """
        url = reverse("register_user")
        data = {
            "username": "common-password",
            "email": "common.password@example.com",
            "password": "qwerty",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_duplicate_username(self):
        """
        Attempt to register a user account with an already existing username.
        """
        CustomUser.objects.create_user(
            "existing-username", "existing.username@example.com", "P4SsW0rdSh0uLdW00Rk"
        )
        url = reverse("register_user")
        data = {
            "username": "existing-username",
            "email": "another.username@example.com",
            "password": "r4Mns&ywn2837",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_duplicate_email(self):
        """
        Attempt to register a user account with an already existing email.
        """
        CustomUser.objects.create_user(
            "existing-username", "existing.username@example.com", "r4Mns&ywn2837"
        )
        url = reverse("register_user")
        data = {
            "username": "another-username",
            "email": "existing.username@example.com",
            "password": "r4Mns&ywn2837",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)
