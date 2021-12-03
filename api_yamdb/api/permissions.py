from rest_framework.permissions import SAFE_METHODS, BasePermission
from users.models import UserRoles


class IsModeratorOrAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and (obj.author == request.user
                 or request.user == obj.author
                 or request.user.role == UserRoles.ADMIN
                 or request.user.role == UserRoles.MODERATOR)
        )


class AdminPermission(BasePermission):

    def has_permission(self, request, view):

        return (request.user.is_superuser
                or (request.auth and request.user.role == UserRoles.ADMIN))


class AdminOrReadOnlyPermission(BasePermission):

    def has_permission(self, request, view):

        return (request.method in SAFE_METHODS
                or (request.auth and request.user.role == UserRoles.ADMIN))
