from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.personnel.models import ManagerModel, StaffModel


class ManagerAdmin(UserAdmin):
    list_display = ("name", "email", "role", "is_admin", "created_at")
    search_fields = ("name", "email", "role")
    readonly_fields = ("is_admin", "created_at")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(ManagerModel)


class StaffAdmin(UserAdmin):
    list_display = ("name", "email", "role", "is_admin", "created_at")
    search_fields = ("name", "email")
    readonly_fields = ("is_admin", "created_at")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(StaffModel)
