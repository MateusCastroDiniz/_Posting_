from rest_framework import serializers
from core.posting.models import Post, PostFile
from .comment_serializer import CommentSerializer
from .post_file_serializer import PostFileSerializer
from .user_serializer import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    files = PostFileSerializer(read_only=True, many=True)
    author_username = serializers.ReadOnlyField(source='author.username')
    profile_picture = serializers.ReadOnlyField(source='author.profile_picture.profile_picture.url')

    class Meta:
        model = Post
        fields = [
            'id',
            'text_content',
            'created_on',
            'updated_on',
            'author_username',
            'files',
            'slug',
            'comments',
            'profile_picture'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text_content = validated_data.get('text_content', instance.text_content)
        PostFile.objects.filter(post=instance).update(arq_content=validated_data.get('files', instance.files))
        instance.save()
        return instance


