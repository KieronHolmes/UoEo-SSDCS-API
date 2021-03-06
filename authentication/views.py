"""
Provides access to the Register functionality of the system.
"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from authentication.models import CustomUser

from .serializers import RegisterSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Register a user account.",
        description="Registers for a new user account with the provided details.",
        tags=["Registration"],
    )
)
class RegisterView(CreateAPIView):
    """
    post:
        Provides an endpoint for a User to register for access to the system.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
