from django.shortcuts import render
from django.views.generic import TemplateView


class TicketRegisterTemplateView(TemplateView):
    template_name = 'ticket_register.html'

    def ticket_register(self, request):
        return render(request, 'ticket_register.html')
