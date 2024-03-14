from rest_framework import serializers
from core.posting.models import Post
from .comment_serializer import CommentSerializer
from .user_serializer import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    author_username = serializers.ReadOnlyField(source='author.username')
    author_avatar = serializers.ReadOnlyField(source='author.avatar.url')

    class Meta:
        model = Post
        fields = [
            'id',
            'text_content',
            'image_content',
            'created_on',
            'updated_on',
            'author_username',
            'slug',
            'comments',
            'author_avatar'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.image_content = validated_data.get('image_content', instance.image_content)
        instance.save()
        return instance


