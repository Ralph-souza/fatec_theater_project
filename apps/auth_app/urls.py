from django.urls import path

from apps.auth_app.views import Login, Register


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]
