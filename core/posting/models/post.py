from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    image_content = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text_content)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-created_on']
