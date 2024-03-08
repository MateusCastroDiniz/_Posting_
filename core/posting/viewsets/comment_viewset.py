from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..models import Comment, Post
from django.shortcuts import render, get_object_or_404, redirect
from ..serializers import CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..forms import CommentForm


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-created_on')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create_comment(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('feed')

    @classmethod
    @action(detail=True, methods=['post'])
    def edit_comment(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.created_by == request.user:
            if request.method == 'POST':
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                    form.save()
                    return redirect('post_detail' + comment_id)
            else:
                form = CommentForm(instance=comment)
                return render(request, 'edit_comment.html', {'form': form})
        else:
            return redirect('post_detail')



def list_comments(requests):
    comments = CommentViewSet.as_view({'get': 'list'})(requests).data
    return render(requests, 'comment_list.html', {'comments': comments})