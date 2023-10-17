from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    