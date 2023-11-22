from rest_framework import serializers
from .models import Task

class CourseTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'max_grade', 'deadline']
