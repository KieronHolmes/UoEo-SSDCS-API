"""
This file handles the filter attributes which can be used on the Document endpoints.
"""
from django_filters import rest_framework as filters

from .models import Documents


class DocumentFilter(filters.FilterSet):
    """
    Allows the user to filter Documents based on pre-defined inputs supplied within GET parameters.
    """

    title = filters.CharFilter(lookup_expr="icontains")
    owner__username = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        """
        Sets the model to be used for the filter, as well as the parameter names to be used as an input for the filter query.
        """

        model = Documents
        fields = ["title", "owner__username"]
