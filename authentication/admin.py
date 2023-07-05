from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.forms import CustomUserChangeForm, RegistrationUserForm
from authentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = RegistrationUserForm
    form = CustomUserChangeForm
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    search_fields = ('id', 'email')
    ordering = ('id',)
    fieldsets = (
        ('User', {'fields': ('id', 'email', 'password', 'first_name', 'last_name', 'created_by')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_admin', 'is_staff')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password", "confirm_password"),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
