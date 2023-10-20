from django.contrib import admin
from .models import Course, Group


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'group', 'owner']
    readonly_fields = ['owner']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_group_courses',]
    fields = ['name', 'get_group_courses']
    readonly_fields = ['get_group_courses', ]


    @admin.display(description='Group Courses')
    def get_group_courses(self, group: Group):
        courses =  Course.objects.filter(group=group)
        return ", ".join([course.name for course in courses])
