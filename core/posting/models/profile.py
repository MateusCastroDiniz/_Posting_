from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from core.settings import AUTH_USER_MODEL


SEX_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Undefined')
)


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
    age = models.DateTimeField()
    avatar = models.URLField(db_index=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICE, default='U', max_length=1)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
