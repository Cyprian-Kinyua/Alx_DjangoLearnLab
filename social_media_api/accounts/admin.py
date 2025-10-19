from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active', 'created_at']
    list_filter = ['is_staff', 'is_active', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
         'fields': ('bio', 'profile_picture', 'followers')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('bio', 'profile_picture', 'email')}),
    )
