from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import permissions

from authentication.models import CustomUser
from .serializers import GDPRSerializer


class SubjectAccessRequestView(ReadOnlyModelViewSet):
    """
    A function to retrieve all data held about the currently logged in user.
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GDPRSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
