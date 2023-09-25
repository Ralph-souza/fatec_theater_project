from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required. Add a valid e-mail address.")

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")
