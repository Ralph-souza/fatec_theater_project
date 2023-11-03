from django.shortcuts import render, redirect

from apps.movies.forms import MoviesForm, RoomsForm, TheatersForm


def movies_view(request):
    context = {}

    if request.POST:
        movie_form = MoviesForm(request.POST)
        room_form = RoomsForm(request.POST)
        theater_form = TheatersForm(request.POST)

        if movie_form.is_valid() and room_form.is_valid() and theater_form.is_valid():
            movie_form.save()
            room_form.save()
            theater_form.save()

            return redirect("movies_list")

    else:
        movie_form = MoviesForm()
        room_form = RoomsForm()
        theater_form = TheatersForm()

    context["movie_form"] = movie_form
    context["room_form"] = room_form
    context["theater_form"] = theater_form

    return render(request, 'movies.html', context)
