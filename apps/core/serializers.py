from rest_framework import serializers
from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ['id', 'name', 'link_id']
        extra_kwargs = {
            'link_id': {
                'read_only': True
            }
        }


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