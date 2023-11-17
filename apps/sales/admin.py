from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.sales.models import SalesModel


class SalesAdmin(UserAdmin):
    list_display = ("room", "movie", "seat", "price")
    search_fields = ("room", "movie")
    readonly_fields = ("seat", "price")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(SalesModel)
