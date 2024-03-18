from django.db import models
from .post import Post
import os

def upload_to(instance, filename):
    extension = os.path.splitext(filename)[1].lower()
    file_name = str(instance.post.slug) + '-' + filename

    if extension in ['.jpg', '.jpeg', '.png']:
        return os.path.join('posts', 'imgs', file_name)

    elif extension in ['.mp4', '.avi', '.mov', '.webm']:
        return os.path.join('posts', 'videos', file_name)

    elif extension == '.gif':
        return os.path.join('posts', 'gifs', file_name)

    else:
        return os.path.join('posts', 'random', file_name)

class PostFile(models.Model):
    post = models.ForeignKey(Post, related_name='files', on_delete=models.CASCADE)
    arq_content = models.FileField(upload_to=upload_to, blank=True, null=True)
    selected_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['selected_on']

    def __str__(self):
        return self.arq_content.name