from rest_framework import serializers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    authors = AuthorSerializer(many=True)

class ResultSerializer(serializers.Serializer):
    query = serializers.CharField()
    query_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    results = ItemSerializer(many=True)

    @extend_schema_field(OpenApiTypes.STR)
    def get_query_url(self, obj):
        return f"https://cds.cern.ch/search?p={obj['query']}&of=recjson&ot=title,authors,creation_date"

    @extend_schema_field(OpenApiTypes.INT)
    def get_count(self, obj):
        return len(obj["results"])
