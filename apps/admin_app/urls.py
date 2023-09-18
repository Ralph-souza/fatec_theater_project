from django.urls import path


from apps.admin_app.views import (
    MoviesRegisterTemplateView,
    RoomsRegisterTemplateView,
    TheatersRegisterTemplateView
)


urlpatterns = [
    path('movies_register/', MoviesRegisterTemplateView.as_view(), name='movies_register'),
    path('rooms_register/', RoomsRegisterTemplateView.as_view(), name='rooms_register'),
    path('theaters_register/', TheatersRegisterTemplateView.as_view(), name='theaters_register'),
]
