from rest_framework import serializers
from core.posting.models import User, Profile
from .user_serializer import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'username',
            'sex',
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

