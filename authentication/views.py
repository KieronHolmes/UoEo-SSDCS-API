from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .models import CustomUser
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    """
    Provide the functionality for a user to register for a new account.
    """
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
