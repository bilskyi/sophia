from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.core.models import Group
from .models import User


class BaseUserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField('get_user_group')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'group', 'role', 'is_verified']
        extra_kwargs = {
            'is_verified': {'read_only': True},
        }

    def get_user_group(self, obj):
        try:
            group = obj.group
            if group:
                group_data = {
                    'name': group.name,
                    'link_id': group.link_id,
                    'courses': []
                }

                for course in group.group_courses.all():
                    course_data = {
                        'id': course.id,
                        'name': course.name,
                        'description': course.description
                    }
                    group_data['courses'].append(course_data)

                return group_data
        except Exception as ex:
            print(ex)

        return None 
    

class UserRegisterSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ['password']
        extra_kwargs = {
            **BaseUserSerializer.Meta.extra_kwargs,
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class VerifyUserOTPSerializer(serializers.Serializer):
    otp = serializers.CharField()