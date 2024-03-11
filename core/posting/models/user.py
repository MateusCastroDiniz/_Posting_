import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from core.settings import DATETIME_FORMAT

SEX_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Undefined')
)


class UserManager(BaseUserManager):
    def _create_user(self, complete_name, username, birthday, email, password, is_staff, is_superuser, sex='U', **extra_fields):
        now = timezone.now()
        if not complete_name:
            raise ValueError(_('A first name must be set'))
        email = self.normalize_email(email)

        user = self.model(complete_name=complete_name ,username=username, sex=sex,
                          birthday=birthday, email=email, is_staff=is_staff,
                          is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, complete_name, username, birthday, email, password, sex='U',
                    is_staff=False, is_superuser=False, **extra_fields):

        return self._create_user(birthday=birthday, username=username, sex=sex,
                                 is_staff=is_staff, is_superuser=is_superuser, complete_name=complete_name,
                                 email=email, password=password, **extra_fields)

    def create_superuser(self, birthday, username, complete_name, sex, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self._create_user(complete_name=complete_name, username=username, sex=sex,
                                 birthday=birthday, email=email, password=password,
                                 **extra_fields)

        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    complete_name = models.CharField(_('complete name'), max_length=60)

    username = models.CharField(_('username'), max_length=15, unique=True,
                                help_text=_('Required. 15 characters or fewer. Letters,'
                                            ' numbers and @/./+/-/_ characters'),
                                validators=[validators.RegexValidator(
                                    re.compile('^[\w.@+-]+$'), _('Enter a valid username.'),
                                    _('invalid'))])

    birthday = models.DateTimeField(_('birthday'))

    email = models.EmailField(_('email address'), max_length=255, unique=True)

    avatar = models.FileField(upload_to='avatars', blank=True)

    sex = models.CharField(_('sex'), choices=SEX_CHOICE, default='U', max_length=1)

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the '
                                                                                 'user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active '
                                                'Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Designates whether this user '
                                                'has confirmed his account.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['complete_name', 'birthday', 'username']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        return str(self.complete_name).split(' ')[0]

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return self.username
