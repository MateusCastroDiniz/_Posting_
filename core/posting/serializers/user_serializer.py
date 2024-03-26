from rest_framework import serializers
from core.posting.models import User
from .profile_picture_serializer import ProfilePictureSerializer

class UserSerializer(serializers.ModelSerializer):
    profile_picture = ProfilePictureSerializer(read_only=True, many=False)

    class Meta:
        model = User
        fields = [
            'complete_name',
            'username',
            'email',
            'birthday',
            'sex',
            'profile_picture'
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.complete_name = validated_data.get('complete_name', instance.complete_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance