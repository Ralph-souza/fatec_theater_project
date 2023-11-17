from django.urls import path
from django.views.generic import TemplateView

from apps.sales.views import sales_view


urlpatterns = [
    path('sale/', sales_view, name='sale'),
]
