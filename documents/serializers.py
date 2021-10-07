from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Documents


class DocumentSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Documents

        fields = ['title', 'document_content', 'created_at', 'updated_at', 'owner']
