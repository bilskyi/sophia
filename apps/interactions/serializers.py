from rest_framework import serializers
from apps.core.models import Course
from .models import Task


class CourseTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'max_grade', 'deadline', 'course']

    def __init__(self, *args, **kwargs):
        user = kwargs['context'].pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['course'].queryset = Course.objects.filter(owner=user)