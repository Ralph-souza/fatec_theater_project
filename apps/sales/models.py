from django.db import models

from apps.movies.models import MoviesModel, RoomsModel

from apps.sales.choices import MoviesPricesChoices, RoomSeatsChoices


class SalesModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey(MoviesModel, related_name="movie_sales", on_delete=models.CASCADE)
    room = models.ForeignKey(RoomsModel, related_name="room_sales", on_delete=models.CASCADE)
    price = models.FloatField(choices=MoviesPricesChoices.choices, default=15.50, blank=False, null=False)
    seat = models.IntegerField(choices=RoomSeatsChoices.choices, default=40, blank=False, null=False)
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.movie} - {self.room} - {self.price}"
    
    def get_available_seats(self):
        available_seats = set(range(1, self.seat + 1))
        booked_seats = SalesModel.objects.filter(is_booked=True).values_list("seat", flat=True)
        available_seats -= set(booked_seats)

        return available_seats
