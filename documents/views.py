from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import DocumentFilter
from .models import Documents
from .pagination import CustomPagination
from .permissions import UserHasAccessToDocument
from .serializers import DocumentSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Gets a list of all documents.",
        description="Gets a list of all documents within the CERN API that the currently logged in user has access to.",
        tags=["Documents"],
    ),
    post=extend_schema(
        summary="Creates a new document.",
        description="Creates a new document with the provided details.",
        tags=["Documents"],
    ),
)
class DocumentList(ListCreateAPIView):
    """
    API for Document retrieval for a list of documents with specific filters
    """

    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DocumentFilter
    queryset = Documents.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        List all documents:
        Allows users with admin or employee privileges to access all documents
        otherwise, it will show only documents owned by the authenticated user
        """
        if self.request.user.role.lower() in ["admin", "employee"]:
            return Documents.objects.all()
        return Documents.objects.filter(owner=self.request.user)

@extend_schema_view(
    get=extend_schema(
        summary="Fetches a specific document.",
        description="Fetches a specific document (Providing the current user has access to the resource).",
        tags=["Documents"],
    ),
    put=extend_schema(
        summary="Performs a full update to a specific document.",
        description="Performs a complete update of a specific document (Providing the current user has access to the resource).",
        tags=["Documents"],
    ),
    patch=extend_schema(
        summary="Performs a partial update to a specific document.",
        description="Performs a partial update to a specific document (Providing the current user has access to the resource).",
        tags=["Documents"],
    ),
    delete=extend_schema(
        summary="Deletes a specific document.",
        description="Performs a delete on a specific document (Providing the current user has access to the resource).",
        tags=["Documents"],
    ),
)
class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    """
    API for Document retrieval for one specific document
    """

    serializer_class = DocumentSerializer
    # using
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (UserHasAccessToDocument,)

    lookup_field = "id"

    def get_queryset(self):
        """
        GET specific document
        Allows users with admin or employee privileges to access all documents
        otherwise, it will show only documents owned by the authenticated user
        """

        if self.request.user.role.lower() in ["admin", "employee"]:
            return Documents.objects.all()
        return Documents.objects.filter(owner=self.request.user)
