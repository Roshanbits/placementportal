# home/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, User, UserRoleMapping

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(UserRoleMapping)
