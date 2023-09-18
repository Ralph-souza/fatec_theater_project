from django.contrib import admin

from apps.admin_app.models import MoviesModel, RoomsModel, TeathersModel


admin.site.register(MoviesModel)
admin.site.register(RoomsModel)
admin.site.register(TeathersModel)
