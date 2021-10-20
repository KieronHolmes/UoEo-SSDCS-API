''' models for the users DB '''

# import required modules
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ''' database definition that inherits from the AbstractUser '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=False)
    role = models.CharField(max_length=10, default="Guest")