from django import forms

from apps.personnel.models import ManagerModel, StaffModel
from apps.account.models import Account


class ManagerForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.ModelChoiceField(queryset=Account.objects.all(), label="E-mail")

    class Meta:
        model = ManagerModel
        fields = ("name", "email")


class StaffForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.ModelChoiceField(queryset=Account.objects.all(), label="E-mail")

    class Meta:
        model = StaffModel
        fields = ("name", "email")
