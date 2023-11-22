from django.shortcuts import render
from django.shortcuts import get_object_or_404
from apps.user.serializers import *
from apps.core import serializers
from apps.core.permissions import *
from .serializers import CourseTaskSerializer
from .models import Task
from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

    

class JoinUserToGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsVerified, IsStudent]
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


class DeleteUserFromGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsVerified]
    
    def delete(self, request, group_pk, user_pk):
        group = get_object_or_404(Group, pk=group_pk)
        user = get_object_or_404(User, pk=user_pk)

        if user.group != group:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                "detail": "User is not a member of this group",
            })

        user.group = None
        user.save()

        return Response({
            'status': 204,
            'message': f'User removed from the group {group.name} successfully'
        })
    

class CourseTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = CourseTaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerified, IsTeacher]

