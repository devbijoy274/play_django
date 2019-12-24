from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class RegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True 
    )
    token = serializers.CharField(
        max_length=255,
        read_only=True
    )
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('emial', {})
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email addr is required')
        
        if password is None:
            raise serializers.ValidationError('A password is required')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password does not exist')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }