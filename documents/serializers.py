from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Documents


class DocumentSerializer(ModelSerializer):
    """ Serializer class for Documents """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Documents

        fields = ['id', 'title', 'document_content', 'created_at', 'updated_at', 'owner']
