from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['complete_name', 'email', 'username']


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment
        fields = '__all__'


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

