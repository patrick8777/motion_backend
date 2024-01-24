# user\models.py
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField("email address", unique=True)
    followees = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="followers", blank=True)

    def __str__(self):
        return self.username

