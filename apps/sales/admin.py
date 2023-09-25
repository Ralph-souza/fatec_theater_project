from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.sales.models import SalesModel


class ManagerAdmin(UserAdmin):
    list_display = ("movie", "room", "theater", "price", "created_at")
    search_fields = ("movie", "theater")
    readonly_fields = ("price", "created_at")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(SalesModel)
