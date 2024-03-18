from django.shortcuts import render, get_object_or_404
from ..models import Post

def edit_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'edit_post.html', {'post': post})
