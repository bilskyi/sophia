from django.shortcuts import get_object_or_404, redirect
from apps.user.serializers import *
from . import serializers
from .permissions import *
from .models import *
from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAdminUser | IsCourseOwner | IsCourseParticipantReadOnly]

    def list(self, request):
        courses = Course.objects.filter(group=request.user.group)
        serializer = self.get_serializer(courses, many=True)

        return Response({
            'status': 200,
            'message': 'The list of your course(s):',
            'data': serializer.data
        })
    
    def create(self, request, *args, **kwargs):
        if request.user.role in (User.Role.TEACHER, User.Role.ADMIN):
            return super().create(request, *args, **kwargs)
        
        return Response({
            'status': 403,
            'message': 'You do not have permission to perfom this action.'
        })


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser | IsGroupParticipantReadOnly | IsCourseOwnerReadOnly]

    def list(self, request):
        if request.user.group:
            groups = Group.objects.filter(pk=request.user.group.pk)
            serializer = self.get_serializer(groups, many=True)

            return Response({
                'status': 200,
                'message': 'The list of your group(s):',
                'data': serializer.data
            })
        
        return Response({
            'status': 404,
            'message': "User does not have a group",
        })
    
    def create(self, request, *args, **kwargs):
        if request.user.role == User.Role.ADMIN:
            return super().create(request, *args, **kwargs)
        
        return Response({
            'status': 403,
            'message': 'You do not have permission to perfom this action.'
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [permissions.IsAdminUser | IsRequestUser]
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('user-detail', pk=request.user.pk)

        return super().list(request, *args, **kwargs)
    

class GetUsersByGroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseUserSerializer
    permission_classes = [IsVerified, permissions.IsAuthenticated, (permissions.IsAdminUser | IsCourseOwner)]

    def get_queryset(self):
        group_id = self.kwargs.get('pk')
        return User.objects.filter(group_id=group_id)