from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ManyToManyField('Group', related_name='students')
    is_student = models.BooleanField(default=True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_teacher = models.BooleanField(default=True)


class Course(models.Model):
    name = models.CharField("Subject", max_length=50)
    description = models.TextField("Description",)
    owner = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name='courses')


class Group(models.Model):
    name = models.CharField(max_length=30)
