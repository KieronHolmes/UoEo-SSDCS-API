from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from authentication.models import CustomUser
from documents.serializers import DocumentSerializer


class GDPRSerializer(ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "documents")
