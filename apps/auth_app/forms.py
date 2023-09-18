from django import forms
from apps.auth_app.models import AdminUserAuthModel


class AdminUserAuthForm(forms.ModelForm):
    class Meta:
        model = AdminUserAuthModel
        fields = (
            'username',
            'email',
            'password'
        )


class AdminUserLoginForm(forms.ModelForm):
    class Meta:
        model = AdminUserAuthModel
        fields = (
            'username',
            'password'
        )
