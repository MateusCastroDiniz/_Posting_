from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..forms import *
from rest_framework.decorators import action


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created_on')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @classmethod
    @action(detail=True, methods=['post'])
    def edit_post(cls, request, slug):
        post = get_object_or_404(Post, pk=Post.objects.get(slug=slug).pk)
        if post.author == request.user:
            if request.method == 'POST':
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                    form.save()
                    return redirect('feed')
            else:
                form = PostForm(instance=post)
                return render(request, 'edit_post.html', {'form': form})
        else:
            return redirect('feed')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You don't have permission to delete this post."},
                            status=status.HTTP_403_FORBIDDEN)


@login_required
def post_list(request):
    feed = PostViewSet.as_view({'get': 'list'})(request).data
    comments = Comment.objects.all().order_by('created_on')
    return render(request, 'feed.html', {'feed': feed, 'comments': comments, 'user': request.user})


@login_required
def explore_list(request):
    feed = PostViewSet.as_view({'get': 'list'})(request).data
    comments = Comment.objects.all().order_by('created_on')
    return render(request, 'explore.html', {'feed': feed, 'comments': comments, 'user': request.user})
