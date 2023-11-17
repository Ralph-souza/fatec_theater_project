from django import forms

from apps.sales.models import SalesModel

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ["movie", "room", "seat", "price"]
        readonly_fields = ["created_at",]
