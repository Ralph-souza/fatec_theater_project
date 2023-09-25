from django.urls import path

from apps.movies.views import movies_register


urlpatterns = [
    path('movies_register/', movies_register, name='movies_register'),
]
