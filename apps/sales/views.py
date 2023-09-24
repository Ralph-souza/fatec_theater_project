from django.shortcuts import render
from django.views.generic import TemplateView


class SalesRegisterTemplateView(TemplateView):
    template_name = 'sales.html'

    def sales_register(self, request):
        return render(request, 'sales.html')
