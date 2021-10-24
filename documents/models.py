"""
Models class to provide a Documents interface.
"""
import uuid

from django.db import models
from encrypted_model_fields.fields import EncryptedTextField


class Documents(models.Model):
    """
    Columns required for the Documents model.
    Upon user deletion, the Document item(s) associated will be deleted using the SQL CASCADE method.s
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    document_content = EncryptedTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "authentication.CustomUser", related_name="documents", on_delete=models.CASCADE
    )

    class Meta:
        """
        When displaying Document items, these should be ordered by the most recently updated by default.
        """

        ordering = ["-updated_at"]
