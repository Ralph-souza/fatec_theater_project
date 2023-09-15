from django.shortcuts import render
from django.views.generic import TemplateView


class Register(TemplateView):
    template_name = 'register.html'

    def register(self, request):
        return render(request, 'register.html')


class Login(TemplateView):
    template_name = 'login.html'

    def login(self, request):
        return render(request, 'login.html')
