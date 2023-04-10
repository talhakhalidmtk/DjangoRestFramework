from rest_framework.permissions import BasePermission


class VerifyCreator(BasePermission):
    """
    Verify whether the current user is the creator or not.
    """

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
