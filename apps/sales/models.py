from django.db import models

from apps.movies.models import MoviesModel, RoomsModel

from apps.sales.choices import MoviesPricesChoices


class SalesModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey(MoviesModel, related_name="movie_sales", on_delete=models.CASCADE)
    room = models.ForeignKey(RoomsModel, related_name="room_sales", on_delete=models.CASCADE)
    seat = models.IntegerField(blank=False, null=False)
    price = models.FloatField(choices=MoviesPricesChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.movie} - {self.room} - {self.seat}"
