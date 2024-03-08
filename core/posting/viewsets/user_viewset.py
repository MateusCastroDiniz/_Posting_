from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action

from ..models import User, Relation, Post
from django.shortcuts import render, redirect, get_object_or_404
from ..serializers import UserSerializer
from ..forms import UserForm




class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @classmethod
    @action(detail=True, methods=['post'])
    def edit_user(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                new_username = form.cleaned_data['username']
                if User.objects.exclude(pk=user.pk).filter(username=new_username).exists():
                    messages.error(request, 'O username já está em uso. Escolha outro.')
                    return redirect('edit_user', pk=request.user.pk)
                form.save()
                return redirect('profile')
        else:
            form = UserForm(instance=user)
        return render(request, 'edit_user.html', {'form': form})

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


@login_required
def user_config(request):
    user = request.user
    user_posts = Post.objects.filter(author=User.objects.get(id=request.user.pk))
    followers = list(map(lambda x: x.follower.username, Relation.objects.filter(followed=User.objects.get(pk=request.user.pk))))
    following = list(map(lambda x: x.followed.username, Relation.objects.filter(follower=User.objects.get(pk=request.user.pk))))
    num_followers = len(followers)
    num_following = len(following)

    context = {
            'username': user.username,
            'email': user.email,
            'followers': followers,
            'following': following,
            'num_following': num_following,
            'num_followers': num_followers,
            'user_posts': user_posts,
    }
    return render(request, 'profile.html', context)
