from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'group', 'role', 'is_verified']

        extra_kwargs = {
            'is_verified': {'read_only': True},
        }


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