from django.shortcuts import render
from . import serializers
from .models import *
from rest_framework import generics, permissions




class GetCourses(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]