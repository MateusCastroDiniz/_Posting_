from rest_framework import serializers
from core.posting.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'birthday'
        ]

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update_user(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('first_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.brithday = validated_data.get('birthday', instance.brithday)
        instance.save()
        return instance
