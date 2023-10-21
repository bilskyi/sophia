from django.contrib import admin
from .models import Course, Group
from apps.user.models import User

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'group', 'owner']
    readonly_fields = ['owner']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_group_courses',]
    fields = ['name', 'get_group_courses', 'get_group_students']
    readonly_fields = ['get_group_courses', 'get_group_students']


    @admin.display(description='Group Courses')
    def get_group_courses(self, group: list[Group]):
        courses =  Course.objects.filter(group=group)
        return ", ".join([course.name for course in courses])

    @admin.display(description='Group Students')
    def get_group_students(self, group: Group):
        students = group.users.all()
        return "\n".join([student.first_name + " " + student.last_name for student in students])