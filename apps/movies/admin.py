from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.movies.models import MoviesModel, RoomsModel, TheatersModel


class MovieAdmin(UserAdmin):
    list_display = ("title", "director", "category", "rating", "created_at")
    search_fields = ("category", "rating")
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MoviesModel)


class RoomsAdmin(UserAdmin):
    list_display = ("name", "seats", "three_d", "created_at")
    search_fields = ("name",)
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(RoomsModel)


class TheaterAdmin(UserAdmin):
    list_display = ("name", "location", "created_at")
    search_fields = ("name", "location")
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(TheatersModel)
