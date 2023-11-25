from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: UserManager = UserManager()

    def __str__(self):
        return self.email
