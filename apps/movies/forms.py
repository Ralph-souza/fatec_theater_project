from django import forms

from apps.movies.models import MoviesModel, RoomsModel


class RoomsForm(forms.ModelForm):

    class Meta:
        model = RoomsModel
        fields = ("room", "seat")


class MoviesForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title")
    director = forms.CharField(max_length=100, label="Director")
    casting = forms.CharField(max_length=100, label="Casting")
    duration = forms.CharField(max_length=100, label="Duration")
    rating = forms.IntegerField(label="Rating")

    class Meta:
        model = MoviesModel
        fields = ("title", "director", "casting", "duration", "category", "room", "price", "rating")
