from django import forms

from apps.movies.models import MoviesModel, RoomsModel, TheatersModel


class MoviesForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title")
    director = forms.CharField(max_length=100, label="Director")
    casting = forms.CharField(max_length=100, label="Casting")
    duration = forms.CharField(max_length=100, label="Duration")
    rating = forms.IntegerField()

    class Meta:
        model = MoviesModel
        fields = ("title", "director", "casting", "duration", "rating")


class RoomsForm(forms.ModelForm):
    seats = forms.IntegerField(label="Seats")
    three_d = forms.BooleanField(label="3D")

    class Meta:
        model = RoomsModel
        fields = ("seats", "three_d")


class TheatersForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Theater Name")
    locations = forms.CharField(max_length=100, label="Location")

    class Meta:
        model = TheatersModel
        fields = ("name", "locations")
