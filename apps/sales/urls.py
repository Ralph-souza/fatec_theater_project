from django.urls import path

from apps.sales.views import SalesRegisterTemplateView


urlpatterns = [
    path('sales_register/', SalesRegisterTemplateView.as_view(), name='sales_register')
]
