from rest_framework import permissions
from apps.user.models import User


class CreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.TEACHER
    