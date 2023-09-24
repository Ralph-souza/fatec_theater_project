from django.contrib import admin

from apps.movies.models import MoviesModel, RoomsModel, TheatersModel


admin.site.register(MoviesModel)
admin.site.register(RoomsModel)
admin.site.register(TheatersModel)
