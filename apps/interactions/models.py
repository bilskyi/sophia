from django.db import models
from apps.core.models import Course


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    max_grade = models.SmallIntegerField()
    deadline = models.DateTimeField(null=True, blank=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title, self.course