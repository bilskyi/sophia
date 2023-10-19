from rest_framework import serializers
from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ['id', 'name',]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description']
        extra_fields = {
            'role': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        user = self.context['request'].user
        course = models.Course.objects.create(**validated_data)
        course.owner.add(user)
        return course