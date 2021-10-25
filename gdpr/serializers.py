"""
File to handle Django serialization of the GDPR functionality.
"""
from rest_framework.serializers import ModelSerializer

from authentication.models import CustomUser
from documents.serializers import DocumentSerializer


class GDPRSerializer(ModelSerializer):
    """
    Class that serializes the GDPR items..
    """

    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        """
        Specifies the default item to use, as well as the fields which are to be returned to the user.
        """

        model = CustomUser
        fields = ("id", "username", "email", "role", "documents")
