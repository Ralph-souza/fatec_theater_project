from django import forms

from apps.sales.choices import RoomSeatsChoices
from apps.sales.models import SalesModel

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ["movie", "room", "seat", "price"]
