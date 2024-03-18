from .user import User
from django.db import models
from django.utils.text import slugify
from core.settings import DATETIME_FORMAT
import string
import random

def gerar_chave(size=12, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(gerar_chave())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-created_on']
