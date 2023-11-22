from django import forms

from apps.sales.models import SalesModel

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ["movie", "room", "seat", "price"]
        widgets = {
            "seat": forms.RadioSelect(attrs={"class": "seat-grid"}),
        }
        readonly_fields = ["created_at",]

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        sale = self.instance
        available_seats = sale.get_available_seats()
        self.fields["seat"].choices = [(seat, seat) for seat in available_seats]
