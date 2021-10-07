import uuid
from django.db import models


class Documents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    document_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('authentication.CustomUser', related_name="documents", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']
