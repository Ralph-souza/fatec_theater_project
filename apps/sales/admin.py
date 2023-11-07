from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.sales.models import SalesModel


class SalesAdmin(UserAdmin):
    list_display = ("movie", "room", "price", "created_at")
    search_fields = ("movie",)
    readonly_fields = ("price", "created_at")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(SalesModel)
