from django.urls import path
from django.views.generic import TemplateView

from apps.sales.views import movie_sales_view, seat_sales_view


urlpatterns = [
    path('movie_sale/', movie_sales_view, name='movie_sale'),
    path('seat_sale/', seat_sales_view, name='seat_sale'),
    path('ticket/', TemplateView.as_view(template_name='ticket.html'), name='ticket')
]
