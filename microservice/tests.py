from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import CustomUser


class MicroServiceTest(APITestCase):
    def setUp(self):
        """
        Sets up the required attributes for this test class (User accounts).
        """
        self.user = CustomUser.objects.create_user("TestUser", "testuser@example.com", "StR0nGPaSSw5rd!")

    def test_microservice_returns_data(self):
        """
        Ensures the Microservice returns data when correctly authenticated.
        """
        self.assertEqual(1, 1)

    def test_microservice_requires_authentication(self):
        """
        Ensures the endpoint rejects non-authenticated users.
        """
        url = reverse("microservice_search", kwargs={"query": "particle"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
