from rest_framework.generics import (CreateAPIView)
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework import permissions


class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
