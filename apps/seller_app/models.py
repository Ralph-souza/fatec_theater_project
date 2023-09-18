from django.db import models


class TicketsModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey('admin_app.MoviesModel', on_delete=models.CASCADE)
    room = models.ForeignKey('admin_app.RoomsModel', on_delete=models.CASCADE)
    teather = models.ForeignKey('admin_app.TeathersModel', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-created_at']

    def __str__(self):
        return self.movie
