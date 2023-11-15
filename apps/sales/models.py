from django.db import models

from apps.movies.models import MoviesModel, RoomsModel


class MovieSalesModel(models.Model):
    sold_room = models.ForeignKey(RoomsModel, related_name="rooms", on_delete=models.CASCADE)
    sold_movie = models.ForeignKey(MoviesModel, related_name="titles", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sold Movie"
        verbose_name_plural = "Sold Movies"
        ordering = ["id"]


class SeatSalesModel(models.Model):
    sold_seat = models.ForeignKey(RoomsModel, related_name="seats", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sold Seat"
        verbose_name_plural = "Sold Seats"
        ordering = ["id"]


class TicketModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie_ticket = models.ForeignKey(MovieSalesModel, related_name="sold_movies", on_delete=models.CASCADE)
    seat_ticket = models.ForeignKey(SeatSalesModel, related_name="sold_seats", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.movie_ticket
