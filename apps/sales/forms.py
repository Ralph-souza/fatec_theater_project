from django import forms

from apps.sales.models import SalesModel

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ["movie", "room", "price"]
        readonly_fields = ["created_at",]

class SeatForm(forms.Form):
    seat = forms.IntegerField(label="Seat")

    class Meta:
        model = SalesModel
        fields = ["seat"]
