from django.db import models


class MoviesPricesChoices(models.IntegerChoices):
    """Available seats choices"""
    PRICE_1 = 15.50, "R$15.50",
    PRICE_2 = 25.50, "R$25.50",
    PRICE_3 = 35.50, "R$35.50"


class RoomSeatsChoices(models.IntegerChoices):
    """Available seats choices"""
    SEAT_1 = 1, "Seat 1",
    SEAT_2 = 2, "Seat 2",
    SEAT_3 = 3, "Seat 3",
    SEAT_4 = 4, "Seat 4",
    SEAT_5 = 5, "Seat 5",
    SEAT_6 = 6, "Seat 6",
    SEAT_7 = 7, "Seat 7",
    SEAT_8 = 8, "Seat 8",
    SEAT_9 = 9, "Seat 9",
    SEAT_10 = 10, "Seat 10",
    SEAT_11 = 11, "Seat 11",
    SEAT_12 = 12, "Seat 12",
    SEAT_13 = 13, "Seat 13",
    SEAT_14 = 14, "Seat 14",
    SEAT_15 = 15, "Seat 15",
    SEAT_16 = 16, "Seat 16",
    SEAT_17 = 17, "Seat 17",
    SEAT_18 = 18, "Seat 18",
    SEAT_19 = 19, "Seat 19",
    SEAT_20 = 20, "Seat 20",
