from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'group', 'role']
    fields = ['email', 'first_name', 'last_name', 'group', 'role']