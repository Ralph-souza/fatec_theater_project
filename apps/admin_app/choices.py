from django.db import models


class CategoryChoices(models.TextChoices):
    """Small group of movies categories choices"""
    HORROR = 'horror', 'Horror'
    COMEDY = 'comedy', 'Comedy'
    DRAMA = 'drama', 'Drama'
    THRILLER = 'thriller', 'Thriller'


class RoomsChoices(models.TextChoices):
    """Available rooms choices"""
    ROOM_1 = 'room_1', 'Room 1'
    ROOM_2 = 'room_2', 'Room 2'
    ROOM_3 = 'room_3', 'Room 3'
