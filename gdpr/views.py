from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from drf_spectacular.utils import extend_schema, extend_schema_view

from authentication.models import CustomUser
from .serializers import GDPRSerializer


class SubjectAccessRequestView(ReadOnlyModelViewSet):
    """
    list:
        x
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GDPRSerializer
    pagination_class = None

    @extend_schema(
        summary="Performs a Subject Access Request.",
        description="Performs a Subject Access Request with the currently logged in users details.",
        tags=["GDPR"]
    )
    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class SubjectErasureRequestView(APIView):
    """
    delete:
        x
    """
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        summary="Performs a Subject Erasure Request",
        description="Deletes all the information held on the currently logged in user (Including User Account).",
        tags=["GDPR"]
    )
    def delete(self, request, *args, **kwaargs):
        user = request.user
        user.delete()

        return Response({"result": "Subject Erasure Request Completed."})
