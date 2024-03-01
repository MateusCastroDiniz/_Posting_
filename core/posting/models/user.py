import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, first_name, last_name, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not first_name:
            raise ValueError(_('A first name must be set'))
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email,
        is_staff=is_staff, is_active=True,
        is_superuser=is_superuser, last_login=now,
        date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, first_name='Default', last_name='Default', password=None, **extra_fields):
        return self._create_user(first_name, last_name, email, password, **extra_fields)

    def create_superuser(self, email=None, first_name='Default', last_name='Default', password=None, **extra_fields):
        user = self._create_user(first_name, last_name, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('first name'), max_length=30)

    last_name = models.CharField(_('last name'), max_length=30)

    email = models.EmailField(_('email address'), max_length=255, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the '
                                                                                 'user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active '
                                                'Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
    help_text=_('Designates whether this user has confirmed his account.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
