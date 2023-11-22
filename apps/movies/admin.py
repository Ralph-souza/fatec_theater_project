from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.movies.models import MoviesModel, RoomsModel


class RoomsAdmin(UserAdmin):
    list_display = ("room", "created_at")
    search_fields = ("room",)
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(RoomsModel)


class MovieAdmin(UserAdmin):
    list_display = ("title", "director", "category", "room", "rating", "created_at")
    search_fields = ("title","room", "category", "rating")
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MoviesModel)
