from django.urls import path

from apps.auth_app.views import (
    AdminLoginTemplateView,
    AdminRegisterCreateView,
    SellerRegisterTemplateView,
    SellerLoginTemplateView
)


urlpatterns = [
    path('admin_register/', AdminRegisterCreateView.as_view(), name='admin_register'),
    path('admin_login/', AdminLoginTemplateView.as_view(), name='admin_login'),
    path('seller_register/', SellerRegisterTemplateView.as_view(), name='seller_register.html'),
    path('seller_login/', SellerLoginTemplateView.as_view(), name='seller_login.html'),
]
