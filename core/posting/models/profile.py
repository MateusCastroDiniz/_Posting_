import re

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.settings import AUTH_USER_MODEL


SEX_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Undefined')
)


class Profile(models.Model):
    email = models.OneToOneField(AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
    username = models.CharField(_('username'), max_length=15, unique=True,
                                help_text=_('Required. 15 characters or fewer. Letters,'
                                            ' numbers and @/./+/-/_ characters'),
                                validators=[validators.RegexValidator(
                                    re.compile('^[\w.@+-]+$'), _('Enter a valid username.'),
                                    _('invalid'))])
    birthday = models.DateTimeField()
    avatar = models.URLField(db_index=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICE, default='U', max_length=1)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Profile'
