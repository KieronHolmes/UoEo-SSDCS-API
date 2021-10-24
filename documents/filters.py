from django_filters import rest_framework as filters

from .models import Documents


class DocumentFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    owner__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Documents
        fields = ['title', 'owner__username']
