from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    """
    Class to handle Serialization of a speific author returned by the CERN API.
    """
    name = serializers.CharField()


class ItemSerializer(serializers.Serializer):
    """
    Class to handle Serialization of a specific item returned by the CERN API.
    """
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    authors = AuthorSerializer(many=True)


class ResultSerializer(serializers.Serializer):
    """
    Class to handle Serialization of the main result instance.
    """
    query = serializers.CharField()
    query_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    results = ItemSerializer(many=True)

    @extend_schema_field(OpenApiTypes.STR)
    def get_query_url(self, obj):
        """
        Returns the URL used to fetch information from the CERN API.
        """
        return f"https://cds.cern.ch/search?p={obj['query']}&of=recjson&ot=title,authors,creation_date"

    @extend_schema_field(OpenApiTypes.INT)
    def get_count(self, obj):
        """
        Outputs the total number of results returned by the CERN API.
        """
        return len(obj["results"])
