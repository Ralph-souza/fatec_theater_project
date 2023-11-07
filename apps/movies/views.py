from django.shortcuts import render, redirect

from apps.movies.forms import MoviesForm, RoomsForm


def movies_view(request):
    context = {}

    if request.POST:
        movie_form = MoviesForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()

            return redirect('rooms')

    else:
        movie_form = MoviesForm()

    context["movie_form"] = movie_form
    return render(request, 'movies.html', context)


def rooms_view(request):
    context = {}

    if request.POST:
        room_form = RoomsForm(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect('added_movie.html')

    else:
        room_form = RoomsForm()

    context["room_form"] = room_form
    return render(request, 'rooms.html', context)

