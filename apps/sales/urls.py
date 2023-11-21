from django.urls import path
from django.views.generic import TemplateView

from apps.sales.views import sales_view, seat_view


urlpatterns = [
    path('sale/', sales_view, name='sale'),
    path("seat/<int:room_id>", seat_view, name="seat"),
    path("ticket/", TemplateView.as_view(template_name="ticket.html"), name="ticket")
]
