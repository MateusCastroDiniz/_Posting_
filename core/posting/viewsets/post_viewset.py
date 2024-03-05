from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created_on')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def edit_post(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('feed')  # Redirecionar de volta para a página de feed após a edição
        else:
            form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You don't have permission to delete this post."},
                            status=status.HTTP_403_FORBIDDEN)

def post_list(request):
    feed = PostViewSet.as_view({'get': 'list'})(request).data
    return render(request, 'feed.html', {'feed': feed, 'user': request.user})
