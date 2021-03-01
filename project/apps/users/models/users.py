from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Пользователи"""
    username = models.CharField('Логин', unique=True, max_length=255)
    email = models.EmailField("Электронная почта", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
