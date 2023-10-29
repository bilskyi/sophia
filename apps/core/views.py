from django.shortcuts import redirect
from apps.user.serializers import *
from . import serializers
from .permissions import *
from .models import *
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAdminUser | IsCourseOwner | IsCourseParticipantSafe]

    def list(self, request):
        courses = Course.objects.filter(group=request.user.group)
        serializer = self.get_serializer(courses, many=True)
        return Response({
            'status': 200,
            'message': 'The list of your course(s):',
            'data': serializer.data
        })


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser | IsGroupParticipant | IsCourseOwnerSafe]

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
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [permissions.IsAdminUser | IsRequestUser]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('user-detail', pk=request.user.pk)
        return super().list(request, *args, **kwargs)


class GetUsersByGroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseUserSerializer
    permission_classes = [permissions.IsAdminUser | IsCourseOwner]

    def get_queryset(self):
        group_id = self.kwargs.get('pk')
        return User.objects.filter(group_id=group_id)
    

class JoinUserToGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
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