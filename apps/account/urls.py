from django.urls import path

from apps.account.views import registration_view, login_view, logout_view


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
