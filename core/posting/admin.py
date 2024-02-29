from django.contrib import admin
from .models import *


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Define quantos formulários em branco devem ser exibidos


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'updated_on', 'slug',)
    search_fields = ['author']
    inlines = [CommentInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'sex', 'email',)
    search_fields = ['user', 'email']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'created_on')
    list_filter = ('post', 'created_on')