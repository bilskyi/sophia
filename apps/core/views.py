from django.shortcuts import render
from . import serializers
from .models import *
from rest_framework import generics

class StudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer