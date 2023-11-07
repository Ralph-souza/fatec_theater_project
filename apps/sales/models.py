from django.db import models

from apps.movies.models import MoviesModel, RoomsModel


class SalesModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey(MoviesModel, related_name="movies_title", on_delete=models.CASCADE)
    room = models.ForeignKey(RoomsModel, related_name="rooms_name", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Sales'
        ordering = ['-created_at']

    def __str__(self):
        return self.movie
