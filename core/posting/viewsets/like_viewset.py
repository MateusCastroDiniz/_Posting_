from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from django.shortcuts import render, redirect, get_object_or_404
from ..models import User, Post, Like
from ..serializers import LikeSerializer

class LikeViewset(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @classmethod
    @action(detail=True, methods=['post'])
    def like_post(self, request, slug):
        liked_by = request.user
        post = Post.objects.get(slug=slug)
        if request.method == 'POST':
            like = Like.objects.create(post=post, liked_by=liked_by)
            return redirect('feed')
        return render(request, 'feed.html') 

    @classmethod
    @action(detail=True, methods=['POST'])
    def dislike(self, request, slug):
        post = Post.objects.get(slug=slug)
        desliked_by = request.user
        if request.method == 'POST':
            like = Like.objects.get(post=post, liked_by=desliked_by)
            like.delete()
            print(request.POST)
            return redirect('feed')
        return render(request, 'feed.html')

    
