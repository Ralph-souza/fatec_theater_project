from django.urls import path


from apps.movies.views import MoviesRegisterTemplateView


urlpatterns = [
    path('movies_register/', MoviesRegisterTemplateView.as_view(), name='movies_register'),
]
