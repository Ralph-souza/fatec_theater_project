from django.shortcuts import render
from django.views.generic import TemplateView


class MoviesRegisterTemplateView(TemplateView):
    template_name = 'movies_register.html'

    def movies_register(self, request):
        return render(request, 'movies_register.html')


class RoomsRegisterTemplateView(TemplateView):
    template_name = 'rooms_register.html'

    def rooms_register(self, request):
        return render(request, 'rooms_register.html')


class TheatersRegisterTemplateView(TemplateView):
    template_name = 'theaters_register.html'

    def theaters_register(self, request):
        return render(request, 'theaters_register.html')
