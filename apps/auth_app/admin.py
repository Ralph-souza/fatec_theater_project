from django.contrib import admin

from apps.auth_app.models import AdminUserAuthModel, SellerUserAuthModel


admin.site.register(AdminUserAuthModel)
admin.site.register(SellerUserAuthModel)
