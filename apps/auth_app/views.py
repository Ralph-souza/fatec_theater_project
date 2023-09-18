from django.shortcuts import render
from django.views.generic import TemplateView


class AdminRegisterTemplateView(TemplateView):
    template_name = 'admin_register.html'

    def admin_register(self, request):
        return render(request, 'admin_register.html')


class AdminLoginTemplateView(TemplateView):
    template_name = 'admin_login.html'

    def admin_login(self, request):
        return render(request, 'admin_login.html')


class SellerRegisterTemplateView(TemplateView):
    template_name = 'seller_register.html'

    def seller_register(self, request):
        return render(request, 'seller_register.html')


class SellerLoginTemplateView(TemplateView):
    template_name = 'seller_login.html'

    def seller_login(self, request):
        return render(request, 'seller_login.html')
