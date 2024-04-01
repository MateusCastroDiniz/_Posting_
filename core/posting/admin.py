from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'sex', 'email', 'is_staff', 'is_trusty', 'profile_picture')
    search_fields = ['usename']
    list_filter = ('is_staff',)

@admin.register(ProfilePicture)
class ProfilePicture(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')


@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ('post', 'arq_content', 'selected_on',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Define quantos formulários em branco devem ser exibidos


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'updated_on', 'slug',)
    search_fields = ['author', 'slug']
    list_filter = ('created_on',)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'created_on', 'updated_on')
    list_filter = ('created_on',)


@admin.register(Relation)
class RelationsAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed')
    search_fields = ['followed']
