from django.urls import path


from apps.admin_app.views import (
    MoviesRegisterTemplateView,
    RoomsRegisterTemplateView,
    TeathersRegisterTemplateView
)


urlpatterns = [
    path('movies_register/', MoviesRegisterTemplateView.as_view(), name='movies_register'),
    path('rooms_register/', RoomsRegisterTemplateView.as_view(), name='rooms_register'),
    path('teathers_register/', TeathersRegisterTemplateView.as_view(), name='teathers_register'),
]
