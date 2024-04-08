from django.db import models
from .post import Post
from .user import User

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['liked_on']

    def __str__(self):
        return self.liked_by.username