from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'group', 'role', 'is_verified']
    list_display_links = ['id', 'email', 'first_name', 'last_name']
    fields = ['email', 'first_name', 'last_name', 'group', 'role', 'is_verified']
    search_fields = ['email', 'first_name', 'last_name', 'group']