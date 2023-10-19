from django.contrib import admin
from .models import Course, Group


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'group', 'owner']
    readonly_fields = ['owner']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ['name']
