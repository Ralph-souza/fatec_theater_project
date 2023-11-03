from django.shortcuts import render

from apps.movies.forms import MoviesForm, RoomsForm, TheatersForms


def movies_view(request):
    # context = {}
    #
    # if request.POST:
    #     movie =
    return render(request, 'home.html')
