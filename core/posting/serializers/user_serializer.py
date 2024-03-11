from rest_framework import serializers
from core.posting.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UserSerializer(serializers.ModelSerializer):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    class Meta:
        model = User
        fields = [
            'complete_name',
            'username',
            'email',
            'birthday',
            'sex',
            'avatar'
        ]

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update_user(self, instance, validated_data):
        instance.complete_name = validated_data.get('complete_name', instance.complete_name)
        instance.username = validated_data.get('username', instance.username)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.email = validated_data.get('email', instance.email)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.brithday = validated_data.get('birthday', instance.brithday)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
