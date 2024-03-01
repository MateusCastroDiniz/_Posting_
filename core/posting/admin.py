from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_trusty')
    search_fields = ['username']
    list_filter = ('is_staff',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Define quantos formulários em branco devem ser exibidos


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'updated_on', 'slug',)
    search_fields = ['author', 'slug']
    list_filter = ('created_on',)
    inlines = [CommentInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'sex',)
    search_fields = ['user']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'created_on')
    list_filter = ('created_on',)