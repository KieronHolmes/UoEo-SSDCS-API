from rest_framework import permissions


class UserHasAccessToDocument(permissions.BasePermission):
    """
    Restricts item access.
    """

    def has_object_permission(self, request, view, obj):
        # validates user role to admit access only for admin and researcher
        # and owners of the document
        return request.user.role.lower() in ["admin", "employee"] or obj.owner == request.user
