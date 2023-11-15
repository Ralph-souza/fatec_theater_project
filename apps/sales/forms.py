from django import forms

from apps.sales.models import MovieSalesModel, SeatSalesModel, TicketModel


class MovieSalesForm(forms.ModelForm):
    sold_room = forms.IntegerField(label="Room")
    sold_movie = forms.CharField(max_length=100, label="Movie")

    class Meta:
        model = MovieSalesModel
        fields = ("sold_room", "sold_movie")


class SeatSalesForm(forms.ModelForm):
    sold_seat = forms.IntegerField(label="Seat")

    class Meta:
        model = SeatSalesModel
        fields = ("sold_seat",)


class TicketForm(forms.ModelForm):
    movie_ticket = forms.IntegerField(label="Movie")
    seat_ticket = forms.IntegerField(label="Seat")

    class Meta:
        model = TicketModel
        fields = ("movie_ticket", "seat_ticket")
        readonly_fields = ("created_at",)
