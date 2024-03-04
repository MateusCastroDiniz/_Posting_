from .post import Post
from .user import User
from django.db import models
from core.settings import DATETIME_FORMAT


class Comment(models.Model):
    content = models.CharField(max_length=180, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_on']
