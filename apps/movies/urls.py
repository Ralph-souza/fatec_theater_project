from django.urls import path

from apps.movies.views import movies_view, rooms_view


urlpatterns = [
    path('movies/', movies_view, name='movies'),
    path('rooms/', rooms_view, name='rooms'),
]
