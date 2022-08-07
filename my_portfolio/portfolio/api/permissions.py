from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    IsAdminOrReadOnly is a custom Django Rest Framework permission class
    that allows Admin users to POST and anonymous to GET
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
