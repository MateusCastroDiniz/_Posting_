from rest_framework.viewsets import ModelViewSet
from ..models import Comment
from django.shortcuts import render
from ..serializers import CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-created_on')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


def list_comments(requests):
    comments = CommentViewSet.as_view({'get': 'list'})(requests).data
    return render(requests, 'comment_list.html', {'comments': comments})