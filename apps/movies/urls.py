from django.urls import path

from apps.movies.views import movies_view


urlpatterns = [
    path('movies/', movies_view, name='movies'),
]
