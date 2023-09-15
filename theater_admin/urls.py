from django.contrib import admin
from django.urls import path, include

from apps.admin_app import views
from apps.auth_app import views
from apps.seller_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.auth_app.urls'), name='auth')
]
