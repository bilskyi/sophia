from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'
        