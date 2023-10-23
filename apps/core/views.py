from django.shortcuts import render
from apps.user.serializers import UserSerializer
from . import serializers
from .permissions import *
from .models import *
from rest_framework import generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAdminOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class GetUsersByGroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsCourseOwner | permissions.IsAdminUser]

    def get_queryset(self):
        group_id = self.kwargs.get('pk')
        return User.objects.filter(group_id=group_id)
    

class JoinUserToGroupView(APIView):
    def post(self, request):
        serializer = serializers.JoinUserToGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link_id = serializer.data['link_id']
 
        if Group.objects.filter(link_id=link_id).exists():
            group = Group.objects.get(link_id=link_id)
            request.user.group = group
            request.user.save()
            
            return Response({
                'status': 200,
                'message': f'User was joined to the group {group.name}',
                'data': serializer.data
            })
        
        return Response({
            'status': 404,
            'message': "We couldn't find such course",
            "data": serializer.data
        })