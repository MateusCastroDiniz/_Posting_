from rest_framework import serializers
from ..models import ProfilePicture


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'
