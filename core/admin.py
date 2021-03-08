from django.contrib import admin
from core import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile)
