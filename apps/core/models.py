from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    name = models.CharField("Subject", max_length=50)
    description = models.TextField("Description",)
    owner = models.ManyToManyField('user.User', related_name='courses')


class Group(models.Model):
    name = models.CharField(max_length=30)
