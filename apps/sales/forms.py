from django import forms

from apps.movies.models import MoviesModel, RoomsModel
from apps.sales.models import SalesModel


class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesModel
        fields = ("room", "movie", "price")
        read_only_fields = ("created_at",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound and "room" in self.data:
            room_id = int(self.data.get("room"))
            self.fields["movie"].queryset = MoviesModel.objects.filter(room=room_id)
            room = RoomsModel.objects.get(pk=room_id).first()
            self.fields["price"].initial = room.price if room else None

        self.fields["price"].widget.attrs["readonly"] = True

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get("room")
        movie = cleaned_data.get("movie")

        if room and movie:
            cleaned_data["price"] = movie.price
        return cleaned_data

    def update_movie_choices(self, room_id):
        movies = MoviesModel.objects.filter(room=room_id)
        self.fields["movie"].queryset = movies
