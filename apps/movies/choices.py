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


class RoomSeatsChoices(models.IntegerChoices):
    """Available seats choices"""
    SEATS_40 = 40, "40 Seats",
    SEATS_50 = 50, "50 Seats",
    SEATS_60 = 60, "60 Seats",


# class MoviesPriceChoices(models.DecimalField):
#     """Available price choices"""
#     PRICE_10 = 10.00, "R$10.00",
#     PRICE_20 = 20.00, "R$20.00",
#     PRICE_30 = 30.00, "R$30.00",
