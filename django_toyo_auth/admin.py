from django.contrib.auth import admin
from django.utils.translation import gettext, gettext_lazy as _


class ToyoUserAdmin(admin.UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('student_id', 'first_name', 'last_name', 'email', 'grade', 'entry_year', 'is_student', 'is_toyo_member', 'is_iniad_member')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('システム情報'), {'fields': ('username', 'password')}),
    )
    readonly_fields = ('grade',)
    list_display = ('username', 'student_id', 'first_name', 'last_name', 'email', 'is_staff', 'created_at')
    list_filter = ('entry_year', 'is_student', 'is_toyo_member', 'is_iniad_member', 'is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('student_id',)
    search_fields = ('student_id', 'username', 'first_name', 'last_name', 'email')


class UUIDToyoUserAdmin(ToyoUserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('student_id', 'first_name', 'last_name', 'email', 'grade', 'entry_year', 'is_student', 'is_toyo_member', 'is_iniad_member')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('システム情報'), {'fields': ('username', 'password', 'uuid')}),
    )
    readonly_fields = ('grade', 'uuid')
