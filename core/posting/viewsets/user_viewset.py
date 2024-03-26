import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from ..models import User, Relation, Post, ProfilePicture
from django.shortcuts import render, redirect, get_object_or_404
from ..serializers import UserSerializer
from ..forms import UserForm, UserCreateForm
from PIL import Image


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all()

    # @classmethod
    # @action(detail=True, methods=['POST'])
    # def edit_user(cls, request, pk=None):
    #     form = UserForm()
    #     if request.method == 'POST':
    #         # print(f'Post Result: {request.POST}')
    #         form = UserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #         # user = User.objects.get(pk=pk)
    #
    #         # data = {'username': request.POST.get('username'), 'profile_picture': request.FILES.get('profile_picture')}
    #         # serializer = UserSerializer(user, data=data)
    #         # if serializer.is_valid():
    #         #     serializer.save()
    #             return redirect('user')
    #     return render(request, 'user_detail.html')

    # @classmethod
    # @action(detail=True, methods=['post'])
    # def edit_user(cls, request, username=None):
    #     if request.method == 'POST':
    #         user = get_object_or_404(User, username=request.user.username)
    #         print(user)
    #         data = {'username': request.POST.get('username'), 'profile_picture': request.FILES.get('profile_picture')}
    #         serializer = UserSerializer(instance=user, data=data)
    #         if serializer.is_valid():
    #             serializer.update()
    #             return redirect('user')
    #     return render(request, 'user_detail.html')

    # @action(detail=True, methods=['post'])
    # def edit_user(self, request, username=None):
    #     user = User.objects.get(username=username)
    #     serializer = self.get_serializer(user)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return redirect('user')
    #     return render(request, 'user_detail.html')

    @classmethod
    @action(detail=True, methods=['post'])
    def signup(cls, request):
        if request.method == 'POST':
            complete_name = request.POST.get('complete_name')
            email = request.POST.get('email')
            birthday = request.POST.get('birthday')
            username = request.POST.get('username')
            password = request.POST.get('password')
            profile_picture = request.FILES.get('profile_picture')

            if User.objects.filter(email=email).exists():
                return messages.error(request, 'Email already exists')
                return redirect('signup')

            # Precisa ser feito um método de exibição in time para preenchimento correto do formulário de cadastro

            if User.objects.filter(username=username).exists():
                return messages.error(request, 'Username already exists')
                return redirect('signup')

            user = User.objects.create_user(username=username, email=email, password=password,
                                            complete_name=complete_name, birthday=birthday)
            user.save()

            picture = ProfilePicture.objects.create(user=user)
            picture.profile_picture = profile_picture
            picture.save()

            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')  # Redirecionar para a página de login após o registro

        return render(request, 'sign_up.html')


@login_required
@action(detail=True, methods=['post'])
def user_config(request):
    user = request.user
    user_posts = Post.objects.filter(author=user) # !!! Já está aqui! Não reinvente a roda!
    profile_picture = ProfilePicture.objects.get(user=request.user).profile_picture.url
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
            'profile_picture': profile_picture
    }
    return render(request, 'user_detail.html', context)


@login_required
@action(detail=True, methods=['post'])
def edit_user(request, username):
    user = User.objects.get(username=username)
    form = UserForm(instance=user)

    if request.method == 'POST':
        print(f'Arquivo enviado via request.FILES: {request.FILES.get("file_content")}')
        form = UserForm(request.POST, instance=user)
        profile_picture = request.FILES.get('file_content')

        if form.is_valid():
            print(form)
            print(profile_picture)
            # im = Image.open(profile_picture)

            # form.save()
            # User.objects.filter(username=user.username).update(username=request.POST.get('username'))
            # edited_user = User.objects.get(username=request.POST.get('username'))

            # edited_user.save()

            # if profile_picture:
            #     current_profile_picture = edited_user.profile_picture

            #     if profile_picture != current_profile_picture.profile_picture:
                
            #         if current_profile_picture:
                
            #             if edited_user.profile_picture and edited_user.profile_picture.profile_picture.url != '/media/default_profile_picture/default_profile_picture.png':
                         
            #                 os.remove(edited_user.profile_picture.profile_picture.path)
            #             edited_user.profile_picture.delete()

            #         profile_pic, created = ProfilePicture.objects.get_or_create(user=edited_user)
            #         profile_pic.profile_picture = profile_picture
            #         profile_pic.save()
            
            # if profile_picture is None:
            #     redirect('user')

            return redirect('user')


        # Estou pensando em separar o campo de atualização de perfil do formulário de edição de username.
        # Ainda não sei se é uma boa ideia...
    data = {'form': form }
    return render(request, 'user_config.html', context=data)


@login_required
def edit_profile_picture(request, username=None):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        new_prof_pictur = request.FILES.get('profile_picture')
        print(new_prof_pictur)

        # if new_prof_pictur:
        #     if user.profile_picture.path != 'media/default_profile_picture/default_profile_picture.png':
        #         os.remove(user.profile_picture.path)
        #     user.profile_picture = new_prof_pictur
        #     user.save()
    return render(request, 'user_config.html')


@login_required
def delete_profile_picture(request):
    user = User.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        
        print(user.profile_picture.profile_picture.url)

        # default_pic = os.path.join('default_profile_picture', 'default_profile_picture.png')

        # user.profile_picture.path = 'media/default_profile_picture/default_profile_picture.png'

        # new_profpic = ProfilePicture.objects.get(user=user)
        # new_profpic.name = default_pic
        # new_profpic.save()

        # if user.profile_picture.profile_picture.url != '/media/default_profile_picture/default_profile_picture.png':
        #     user.profile_picture.delete()

        # profile_pic, created = ProfilePicture.objects.get_or_create(user=user)
        # profile_pic.save()

        # user.save()
        return redirect('user')

    return render(request, 'user_config.html')