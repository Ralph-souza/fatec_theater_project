from django.urls import path
from django.views.generic import TemplateView

from apps.movies.views import movies_view, rooms_view


urlpatterns = [
    path('movies/', movies_view, name='movies'),
    path('rooms/', rooms_view, name='rooms'),
    path('movies/success/', TemplateView.as_view(template_name='success.html'), name='success')
]
