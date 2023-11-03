from django.urls import path

from apps.sales.views import sales_view


urlpatterns = [
    path('sales/', sales_view, name='sales')
]
