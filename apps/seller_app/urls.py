from django.urls import path

from apps.seller_app.views import TicketRegisterTemplateView


urlpatterns = [
    path('ticket_register/', TicketRegisterTemplateView.as_view(), name='ticket_register')
]
