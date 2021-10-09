from django_filters import rest_framework as filters
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import DocumentFilter
from .models import Documents
from .pagination import CustomPagination
from .serializers import DocumentSerializer


# Create your views here.
class DocumentList(ListCreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DocumentFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Documents.objects.filter(owner=self.request.user)


class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Documents.objects.filter(owner=self.request.user)
