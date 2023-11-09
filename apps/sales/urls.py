from django.urls import path
from django.views.generic import TemplateView

from apps.sales.views import sales_view


urlpatterns = [
    path('sales/', sales_view, name='sales'),
    path('sales/ticket/', TemplateView.as_view(template_name='ticket.html'), name='ticket')
]
