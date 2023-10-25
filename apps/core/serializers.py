from rest_framework import serializers
from . import models


class GroupSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField('get_courses')

    class Meta:
        model = models.Group
        fields = ['id', 'name', 'link_id', 'courses']
        extra_kwargs = {
            'link_id': {
                'read_only': True
            }
        }
    
    def get_courses(self, obj):
        courses = obj.group_courses.all()
        course_data = []
        for course in courses:
            course_data.append({
                'id': course.id,
                'name': course.name,
                'description': course.description
            })
        return course_data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'group', 'owner']
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        user = self.context['request'].user
        course = models.Course.objects.create(**validated_data)
        course.owner.add(user)
        return course
    

class JoinUserToGroupSerializer(serializers.Serializer):
    link_id = serializers.CharField(max_length=6)