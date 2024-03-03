from rest_framework import serializers
from core.posting.models import Comment, Post
from .comment_serializer import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            'text_content',
            'image_content',
            'created_on',
            'updated_on',
            'author',
            'slug',
            'comments'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.save()
        return instance


