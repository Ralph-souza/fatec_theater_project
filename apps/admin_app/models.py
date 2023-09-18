from django.db import models

from apps.admin_app.choices import CategoryChoices, RoomsChoices


class MoviesModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    director = models.CharField(max_length=100, blank=False, null=False)
    casting = models.CharField(max_length=100, blank=False, null=False)
    duration = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(choices=CategoryChoices.choices, max_length=50, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['id']

    def __str__(self):
        return self.title


class RoomsModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(choices=RoomsChoices.choices, max_length=100, blank=False, null=False)
    seats = models.IntegerField(blank=False, null=False)
    three_d = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        ordering = ['id']

    def __str__(self):
        return self.name


class TeathersModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    titles = models.ForeignKey("admin_app.MoviesModel", on_delete=models.CASCADE)
    rooms = models.ForeignKey("admin_app.RoomsModel", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Theater'
        verbose_name_plural = 'Theaters'
        ordering = ['id']

    def __str__(self):
        return self.name
