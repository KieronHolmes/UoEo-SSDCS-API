"""
Handles Document CRUD permissions.
"""
from rest_framework import permissions


class UserHasAccessToDocument(permissions.BasePermission):
    """
    Determines whether a User can access the specified Document resource.
    """
    def has_object_permission(self, request, view, obj):
        """
        Determines whether the current user has access to the object requested.
        Admin/Employees will be able to use all CRUD functionality available to the Document model, whereas Researchers can only modify documents they own.
        """
        return (
            request.user.role.lower() in ["admin", "employee"]
            or obj.owner == request.user
        )
