"""
Provides access to the Microservice functionality of the system.
"""
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import GDPRSerializer


class SubjectAccessRequestView(ReadOnlyModelViewSet):
    """
    list:
        Returns all data held about the currently logged-in User, including all Documents.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GDPRSerializer
    pagination_class = None

    @extend_schema(
        summary="Performs a Subject Access Request.",
        description="Performs a Subject Access Request with the currently logged in users details.",
        tags=["GDPR"],
    )
    def list(self, request, *args, **kwargs):
        """
        Fetches and Serializes all data held about the currently logged-in user.
        """
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class SubjectErasureRequestView(APIView):
    """
    delete:
        Deletes the currently authenticated user. All Documents will be deleted using the SQL databases CASCADE
        functionality.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = None

    @extend_schema(
        summary="Performs a Subject Erasure Request",
        description="Deletes all the information held on the currently logged in user (Including User Account).",
        tags=["GDPR"],
    )
    def delete(self, request, *args, **kwaargs):
        """
        Deletes the currently authenticated user.
        """
        user = request.user
        user.delete()

        return Response({"result": "Subject Erasure Request Completed."})
