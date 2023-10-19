from django.shortcuts import render
from . import serializers
from .permissions import *
from .models import *
from rest_framework import generics, permissions, viewsets


class GetCoursesView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateCourseView(generics.CreateAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [CreateCourse]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAdminOrReadOnly]
