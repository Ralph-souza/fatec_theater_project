from django.db import models


class MoviesPricesChoices(models.IntegerChoices):
    """Available seats choices"""
    PRICE_1 = 15.50, "R$15.50",
    PRICE_2 = 25.50, "R$25.50",
    PRICE_3 = 35.50, "R$35.50"
