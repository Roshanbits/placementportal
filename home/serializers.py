# home/serializers.py
from rest_framework import serializers
from .models import Role, User, UserRoleMapping
from django.contrib.auth import authenticate

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'password', 'roles']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        user = User.objects.create_user(**validated_data)
        for role_name in roles_data:
            role, created = Role.objects.get_or_create(name=role_name)
            UserRoleMapping.objects.create(user=user, role=role)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid username or password.')
        return {'user': user}