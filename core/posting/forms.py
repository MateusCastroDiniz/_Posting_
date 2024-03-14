from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_content']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['complete_name', 'email', 'username', 'avatar']


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment
        fields = ['__all__']

