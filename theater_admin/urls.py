from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls'), name='register'),
    path('movies/', include('apps.movies.urls'), name='movies'),
    path('personnel/', include('apps.personnel.urls'), name='personnel'),
    path('sales/', include('apps.sales.urls'), name='sales'),
]
