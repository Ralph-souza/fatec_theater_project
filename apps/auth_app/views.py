from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from apps.auth_app.forms import AdminUserAuthForm, AdminUserLoginForm


class AdminRegisterCreateView(generic.CreateView):
    template_name = 'admin_register.html'
    form_class = AdminUserAuthForm
    success_url = reverse_lazy('admin_login')


class AdminLoginTemplateView(generic.View):
    template_name = 'admin_login.html'
    form_class = AdminUserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {{'form': form}})


class SellerRegisterTemplateView(generic.TemplateView):
    template_name = 'seller_register.html'

    def seller_register(self, request):
        return render(request, 'seller_register.html')


class SellerLoginTemplateView(generic.TemplateView):
    template_name = 'seller_login.html'

    def seller_login(self, request):
        return render(request, 'seller_login.html')
