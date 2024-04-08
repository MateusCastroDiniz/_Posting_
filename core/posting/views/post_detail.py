from django.views import generic
from ..models import Post, Comment, ProfilePicture

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post).order_by('created_on')
        context['profile_picture'] = ProfilePicture.objects.get(user=post.author.id).profile_picture.url
        return context

    def delete_comment(self, request, id):
        comment = Comment.objects.get(id=id)
        if request.method == 'POST':
            print(comment)
            comment.delete()
            return redirect('post_detail', slug=slug)