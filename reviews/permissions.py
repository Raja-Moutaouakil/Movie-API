from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow object owners to edit; others read-only."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `user`.
        return getattr(obj, 'user', None) == request.user


class IsSelfOrAdmin(permissions.BasePermission):
    """Allow users to access/modify their own user object or admins."""

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return obj == request.user
