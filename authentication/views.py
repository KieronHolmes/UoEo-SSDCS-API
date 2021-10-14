from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .models import CustomUser
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
