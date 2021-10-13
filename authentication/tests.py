from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser


class RegisterTests(APITestCase):
    def test_register_valid(self):
        """Register a valid user account."""
        url = reverse('register_user')
        data = {
            'username': 'valid-user',
            'password': 'r4nD0mPaSsW0rrd#0192',
            'email': 'valid.user@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'valid-user')

    def test_register_invalid(self):
        """Attempt to register an invalid user account."""
        url = reverse('register_user')
        data = {
            'username': 'invalid-user',
            'email': 'ThisIsNotAnEmailAddress',
            'password': 'StR0nGP45SWorD'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_common_password(self):
        """Attempt to register a user account with a commonly used password."""
        url = reverse('register_user')
        data = {
            'username': 'common-password',
            'email': 'common.password@example.com',
            'password': 'qwerty'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_duplicate_username(self):
        """Attempt to register a user account with an already existing username"""
        CustomUser.objects.create_user(
            'existing-username',
            'existing.username@example.com',
            'P4SsW0rdSh0uLdW00Rk'
        )
        url = reverse('register_user')
        data = {
            'username': 'existing-username',
            'email': 'another.username@example.com',
            'password': 'P4SsW0rdSh0uLdW00Rk'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_duplicate_email(self):
        """Attempt to register a user account with an already existing email."""
        CustomUser.objects.create_user(
            'existing-username',
            'existing.username@example.com',
            'P4SsW0rdSh0uLdW00Rk'
        )
        url = reverse('register_user')
        data = {
            'username': 'another-username',
            'email': 'existing.username@example.com',
            'password': 'P4SsW0rdSh0uLdW00Rk'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)
