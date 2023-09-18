from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_app/', include('apps.auth_app.urls'), name='auth_app'),
    path('admin_app/', include('apps.admin_app.urls'), name='admin_app'),
    path('seller_app/', include('apps.seller_app.urls'), name='seller_app'),
]
