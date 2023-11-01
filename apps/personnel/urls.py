from django.urls import path

from apps.personnel.views import profile_view


urlpatterns = [
    path('profile/', profile_view, name='profile'),
]
