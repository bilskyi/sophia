from django.shortcuts import render
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
