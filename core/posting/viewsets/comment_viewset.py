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

    @classmethod
    @action(detail=True, methods=['post'])
    def create_comment(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            print(post)
            comment = Comment.objects.create(post=post, content=request.POST.get('content'), created_by=request.user)
            comment.save()
            # form = CommentForm(request.POST, instance=post)
            # if form.is_valid():
            #     form.save()
            return redirect('post_detail', slug=slug)

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
    
    @classmethod
    @action(detail=True, methods=['post'])
    def delete_comment(self, request, id):
        comment = Comment.objects.get(id=id)
        post_slug = comment.post.slug
        if request.method == 'POST':
            print(comment)
            comment.delete()
            return redirect('post_detail', slug=post_slug)



def list_comments(requests):
    comments = CommentViewSet.as_view({'get': 'list'})(requests).data
    return render(requests, 'comment_list.html', {'comments': comments})