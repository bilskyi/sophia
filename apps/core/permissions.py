from rest_framework import permissions
from apps.user.models import User
from .models import Course


class IsVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_verified


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == User.Role.TEACHER


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminOrReadOnly,
            self).has_permission(request, view)
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin
    

class IsCourseOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == User.Role.TEACHER:
                has_courses_with_group = Course.objects.filter(owner=request.user, group_id=view.kwargs.get('pk')).exists()
                if has_courses_with_group:
                    return True
    
        return False