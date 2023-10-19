from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'owner']
    readonly_fields = ['owner']