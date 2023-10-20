from django.shortcuts import render

from apps.user.serializers import UserSerializer
from . import serializers
from .permissions import *
from .models import *
from rest_framework import generics, permissions, viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAdminOrReadOnly]


class GetUsersByGroupView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [GetUsersByGroup | permissions.IsAdminUser]
    

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        return User.objects.filter(group=group_id)