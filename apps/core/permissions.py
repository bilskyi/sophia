from rest_framework import permissions
from apps.user.models import User


class CreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.TEACHER
    

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminOrReadOnly, 
            self).has_permission(request, view)
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin