from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'max_grade', 'deadline', 'course']
    list_display_links = list_display