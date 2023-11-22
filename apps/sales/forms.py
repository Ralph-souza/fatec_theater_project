from django import forms

from apps.sales.models import SalesModel

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ["movie", "room", "seat", "price"]
        readonly_fields = ["created_at",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        room_instance = self.initial.get("room")
        if room_instance:
            seats_choice = [(i, f"{i} seats") for i in range(1, room_instance.seat + 1)]
            self.fields["seat"].choices = seats_choice

        self.fields["is_booked"] = forms.BooleanField(initial=False, required=False)
        
    def save(self, commit=True):
        instance = super().save(commit=False)

        is_booked = self.cleaned_data["is_booked"]
        if is_booked:
            instance.is_booked = True

        if commit:
            instance.save()

        return instance
