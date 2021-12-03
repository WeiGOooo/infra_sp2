from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )


class User(AbstractUser):
    bio = models.TextField('BIO', blank=True, max_length=2000)
    username = models.CharField(
        'NIK', unique=True, max_length=20, blank=True)
    email = models.EmailField('EMAIL', unique=True, blank=False)
    role = models.CharField('ROLE', choices=UserRoles.choices,
                            default=UserRoles.USER, max_length=10)
    confirmation_code = models.CharField(
        'SECURE CODE', blank=True, null=True, editable=False,
        unique=True, max_length=100)

    def __str__(self):
        return self.username
