

from rest_framework import serializers
from .models import Profile
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.conf import settings

# Get the custom user model
User = get_user_model()

# Serializer to represent the CustomUser model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id',  'username','email','birth_date','bio', 'stans', 'stanning',)

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password field is included and write-only

    class Meta:
        model = Profile
        fields = ('user_id', 'username', 'email', 'birth_date', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Profile(
            username=validated_data['username'],
            email=validated_data['email'],
            birth_date=validated_data['birth_date'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializer for user login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Accept phone number as input
    password = serializers.CharField()  # Accept password as input

    # Validate user credentials
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)  # Authenticate user

        # If authentication fails or user is inactive, raise a validation error
        if user is None or not user.is_active:
            raise serializers.ValidationError("Invalid credentials")

        return user
