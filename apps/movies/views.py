from django.shortcuts import render
from django.views.generic import TemplateView


class MoviesRegisterTemplateView(TemplateView):
    template_name = 'index.html'

    def movies_register(self, request):
        return render(request, 'index.html')
