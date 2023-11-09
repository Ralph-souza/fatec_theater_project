from django import forms

from apps.movies.models import MoviesModel, RoomsModel
from apps.sales.models import SalesModel


class SalesForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=RoomsModel.objects.all(), label="Room")
    movie = forms.ModelChoiceField(queryset=MoviesModel.objects.none(), label="Movie")

    class Meta:
        model = SalesModel
        fields = ("room", "movie", "price")
        read_only_fields = ("created_at",)

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        if "room" in self.data:
            room_id = int(self.data.get("room"))
            self.fields["movie"].queryset = MoviesModel.objects.filter(room=room_id)

        self.fields["price"].widget.attrs["readonly"] = True

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get("room")

        if room:
            cleaned_data["price"] = room.price
        return cleaned_data

    def update_movie_choices(self, room_id):
        movies = MoviesModel.objects.filter(room=room_id)
        self.fields["movie"].queryset = movies
