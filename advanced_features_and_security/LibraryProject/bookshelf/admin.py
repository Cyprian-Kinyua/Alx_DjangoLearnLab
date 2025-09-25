from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Book, CustomUser


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_year')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email',
                    'date_of_birth', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Book)
