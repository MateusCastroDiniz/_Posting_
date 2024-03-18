import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from ..models import User, Relation, Post
from django.shortcuts import render, redirect, get_object_or_404
from ..serializers import UserSerializer
from ..forms import UserForm, UserCreateForm


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=False, methods=['POST'])
    # def edit_user(self, request):
    #     user = get_object_or_404(User, pk=User.objects.get(pk=request.user.id).pk)
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         avatar = request.FILES.get('avatarUpload')  # Corrigido para corresponder ao nome do campo no formulário

    #         new_username = username
    #         if User.objects.exclude(pk=user.pk).filter(username=new_username).exists():
    #             messages.error(request, 'O username já está em uso. Escolha outro.')
    #             return redirect('edit_user', pk=request.user.pk)
    #         else:
    #             user.username = new_username

    #         if avatar:
    #             if user.avatar.path != '/media/default-avatars/default-avatar.png':
    #                 os.remove(user.avatar.path)
    #             user.avatar = avatar

    #         user.save()
    #         return redirect('user')
    #     else:
    #         return render(request, 'edit_user.html', {'user': user})
    @classmethod
    @action(detail=False, methods=['post'])
    def edit_user(self, request):
        user = get_object_or_404(User, pk=request.user.pk)

        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            new_username = form.cleaned_data['username']
            
            if User.objects.exclude(pk=user.pk).filter(username=new_username).exists():
                messages.error(request, 'O username já está em uso. Escolha outro.')
                return redirect('edit_user')

            if request.FILES.get('avatar'):
                new_avatar = request.FILES.get('avatar')
                if user.avatar.path != '/media/default-avatars/default-avatar.png':
                    os.remove(user.avatar.path)
                user.avatar = new_avatar

            form.save()
            return redirect('user')
        else:
            form = UserForm(instance=user)
        
        return render(request, 'edit_user.html', {'form': form})




    @classmethod
    @action(detail=True, methods=['post'])
    def signup(cls, request):
        if request.method == 'POST':
            complete_name = request.POST.get('complete_name')
            email = request.POST.get('email')
            birthday = request.POST.get('birthday')
            username = request.POST.get('username')
            password = request.POST.get('password')
            avatar = request.FILES.get('avatar')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')

            user = User.objects.create_user(username=username, email=email, password=password,
                                            complete_name=complete_name, birthday=birthday, avatar=avatar)
            user.save()

            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')  # Redirecionar para a página de login após o registro

        return render(request, 'sign_up.html')

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


@login_required
def user_config(request):
    user = request.user
    user_posts = Post.objects.filter(author=User.objects.get(id=request.user.pk)) # !!! Já está aqui! Não reinvente a roda!
    user_avatar = User.objects.get(id=user.pk).avatar.url
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
            'user_avatar': user_avatar
    }
    return render(request, 'user_detail.html', context)
