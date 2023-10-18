from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)

#     def save(self, *args, **kwargs):
#         if self.is_student and self.is_teacher:
#             raise ValueError('A user cannot be both a student and a teacher.')
#         super(User, self).save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField("Subject", max_length=50)
    description = models.TextField("Description",)
    owner = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name='courses')


class Group(models.Model):
    name = models.CharField(max_length=30)
