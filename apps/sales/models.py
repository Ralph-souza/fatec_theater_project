from django.db import models


class SalesModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey('movies.MoviesModel', on_delete=models.CASCADE)
    room = models.ForeignKey('movies.RoomsModel', on_delete=models.CASCADE)
    theater = models.ForeignKey('movies.TheatersModel', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Sales'
        ordering = ['-created_at']

    def __str__(self):
        return self.movie