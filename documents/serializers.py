"""
File to handle Django serialization of the Document functionality.
"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Documents


class DocumentSerializer(ModelSerializer):
    """
    Class that serializes a Document item.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Sets the Model and Fields to be used for serialization.
        """
        model = Documents

        fields = [
            "id",
            "title",
            "document_content",
            "created_at",
            "updated_at",
            "owner",
        ]
