from django.urls import path

from apps.sales.views import sales_register


urlpatterns = [
    path('sales_register/', sales_register, name='sales_register')
]
