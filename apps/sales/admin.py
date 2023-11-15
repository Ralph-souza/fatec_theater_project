from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.sales.models import MovieSalesModel, SeatSalesModel, TicketModel


class MovieSalesAdmin(UserAdmin):
    list_display = ("sold_room", "sold_movie")
    search_fields = ("sold_movie",)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MovieSalesModel)


class SeatSalesAdmin(UserAdmin):
    list_display = ("sold_seat",)
    search_fields = ("sold_seat",)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(SeatSalesModel)


class TicketAdmin(UserAdmin):
    list_display = ("movie_ticket", "seat_ticket")
    search_fields = ("movie_ticket",)
    readonly_fields = ("created_at",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(TicketModel)
