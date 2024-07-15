from rest_framework import permissions
from users.models import UserRoles


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки,
     является ли пользователь владельцем объекта или администратором.
    """

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or
                request.user.role == UserRoles.ADMIN.value)


class IsAdminUser(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки,
     является ли пользователь администратором.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == UserRoles.ADMIN.value
