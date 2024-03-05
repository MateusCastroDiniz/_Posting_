from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_content']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['']