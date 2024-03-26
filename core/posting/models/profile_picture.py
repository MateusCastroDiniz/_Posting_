from django.db import models
from .user import User
import os


class ProfilePicture(models.Model):
    profile_picture = models.FileField(upload_to='profile_pictures', blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile_picture', on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_picture.url

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            default_profile_picture_path = os.path.join('default_profile_picture', 'default_profile_picture.png')
            self.profile_picture.name = default_profile_picture_path
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
