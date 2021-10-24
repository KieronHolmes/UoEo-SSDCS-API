"""
Models class to provide a User interface.
"""
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    CustomUser class based on the Django default AbstractUser class.
    This provides the enhanced ID (UUID v4 instead of Incrementing Integers) as well as the User Role column.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10)
