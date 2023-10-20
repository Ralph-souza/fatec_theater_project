from django.urls import path

from apps.personnel.views import manager_view


urlpatterns = [
    path('manager/', manager_view, name="manager")
]
