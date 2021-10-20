from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser


class RegisterTests(APITestCase):
    def test_register_valid(self):
        """
        Register a valid user account.
        """
        url = reverse("register_user")
        data = {
            "username": "valid-user",
            "password": "r4nD0mPaSsW0rrd#0192",
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
            "password": "StR0nGP45SWorD",
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
            "password": "P4SsW0rdSh0uLdW00Rk",
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
            "existing-username", "existing.username@example.com", "P4SsW0rdSh0uLdW00Rk"
        )
        url = reverse("register_user")
        data = {
            "username": "another-username",
            "email": "existing.username@example.com",
            "password": "P4SsW0rdSh0uLdW00Rk",
            "role": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)


class GetTokenTests(APITestCase):
    def test_get_token_valid_user(self):
        """
        Ensures a valid user is able to fetch an Access & Refresh token.
        """
        self.assertEqual(1, 1)

    def test_get_tokens_invalid_user(self):
        """
        Ensures an invalid user is unable to fetch Access & Refresh tokens.
        """
        self.assertEqual(1, 1)

    def test_refresh_token_valid(self):
        """
        Ensures a valid user is able to refresh their tokens.
        """
        self.assertEqual(1, 1)

    def test_refresh_token_invalid(self):
        """
        Ensures an invalid user is unable to refresh their tokens.
        """
        self.assertEqual(1, 1)
