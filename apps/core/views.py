from django.shortcuts import render
from . import serializers, permissions
from .models import *
from rest_framework import generics


class CreateCourse(generics.CreateAPIView):
    permission_classes =  [permissions.IsTeacher]


class GetCourses(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsStudent, permissions.IsTeacher]