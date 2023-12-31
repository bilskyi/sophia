from django.contrib import admin
from .models import Course, Group
from apps.user.models import User

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'group']
    list_display_links = ['id', 'name',]
    fields = ['name', 'description', 'group', 'owner']
    readonly_fields = ['owner']
    search_fields = ['name', 'description']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_group_courses', 'link_id']
    list_display_links = ['id', 'name']
    fields = ['name', 'link_id', 'get_group_courses', 'get_group_students']
    readonly_fields = ['get_group_courses', 'get_group_students', 'link_id']
    search_fields = ['name', 'link_id']


    @admin.display(description='Group Courses')
    def get_group_courses(self, group: list[Group]):
        courses =  Course.objects.filter(group=group)
        return ", ".join([course.name for course in courses])

    @admin.display(description='Group Students')
    def get_group_students(self, group: Group):
        students = group.users.all()
        return "\n".join([student.first_name + " " + student.last_name for student in students])