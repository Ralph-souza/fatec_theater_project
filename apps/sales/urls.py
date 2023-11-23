from django.urls import path

from apps.sales.views import sales_view, ticket_view


urlpatterns = [
    path('sale/', sales_view, name='sale'),
    path("ticket/", ticket_view, name="ticket")
]
