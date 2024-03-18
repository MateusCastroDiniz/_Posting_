from rest_framework import serializers
from core.posting.models import PostFile


class PostFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostFile
        fields = [
            'post_id',
            'arq_content',
            'selected_on',
        ]
