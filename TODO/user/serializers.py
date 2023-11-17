from rest_framework import serializers
from .models import CustomUser, Profile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'email')
