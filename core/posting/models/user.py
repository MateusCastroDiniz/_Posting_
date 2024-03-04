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
    def _create_user(self, first_name, last_name, username, sex, birthday, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not first_name:
            raise ValueError(_('A first name must be set'))
        email = self.normalize_email(email)

        user = self.model(first_name=first_name, last_name=last_name, username=username, sex=sex,
                          birthday=birthday, email=email, is_staff=is_staff,
                          is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, birthday, username, sex, email=None, first_name='Default',
                    last_name='Default', password=None, **extra_fields):

        return self._create_user(birthday=birthday, username=username, sex=sex,
                                 first_name=first_name, last_name=last_name,
                                 email=email, password=password, **extra_fields)

    def create_superuser(self, birthday, username, sex, email=None, first_name='Default',
                         last_name='Default', password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self._create_user(first_name=first_name,
                                 last_name=last_name, username=username, sex=sex,
                                 birthday=birthday, email=email, password=password,
                                 **extra_fields)

        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('first name'), max_length=30)

    last_name = models.CharField(_('last name'), max_length=30)

    username = models.CharField(_('username'), max_length=15, unique=True,
                                help_text=_('Required. 15 characters or fewer. Letters,'
                                            ' numbers and @/./+/-/_ characters'),
                                validators=[validators.RegexValidator(
                                    re.compile('^[\w.@+-]+$'), _('Enter a valid username.'),
                                    _('invalid'))])

    birthday = models.DateTimeField(_('birthday'))

    email = models.EmailField(_('email address'), max_length=255, unique=True)

    avatar = models.URLField(db_index=True, blank=True)

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
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'sex', 'username']
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
