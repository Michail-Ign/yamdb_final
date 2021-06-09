from django.contrib.auth.models import AbstractUser
from django.db import models

from api.managers import UserManager


class Role(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Адрес e-mail',
        unique=True,
        blank=False,
    )
    role = models.CharField(
        max_length=30,
        verbose_name='Роль пользователя',
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        max_length=50,
        blank=True,
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR

    @property
    def is_admin(self):
        return (self.role == Role.ADMIN
                or self.is_staff
                or self.is_superuser)

    def __str__(self):
        return f'{self.role} {self.username}'

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class TempAuth(models.Model):
    email = models.EmailField(
        max_length=254,
        verbose_name='email address',
        unique=True,
    )
    conf_code = models.CharField(
        max_length=62,
        verbose_name='confirmation code',
    )
