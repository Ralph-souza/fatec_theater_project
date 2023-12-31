from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from apps.personnel.choices import RoleChoices
from apps.personnel.models import ManagerModel, StaffModel
from apps.account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            request.session["email"] = email
            return redirect("profile")
        else:
            context["registration_form"] = form
    else:
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "register.html", context)


def login_view(request):
    context = {}
    user = request.user
    redirect_url = None

    if user.is_authenticated:
        try:
            manager = ManagerModel.objects.filter(email=user.email).first()
            if manager.role == RoleChoices.MANAGER:
                redirect_url = "rooms"
        except ManagerModel.DoesNotExist:
            pass
        try:
            staff = StaffModel.objects.filter(email=user.email).first()
            if staff.role == RoleChoices.STAFF:
                redirect_url = "sale"
        except StaffModel.DoesNotExist:
            pass

        if redirect_url:
            return redirect(redirect_url)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                try:
                    manager = ManagerModel.objects.filter(email=user.email).first()
                    if manager and manager.role == RoleChoices.MANAGER:
                        return redirect("rooms")
                except ManagerModel.DoesNotExist:
                    pass
                try:
                    staff = StaffModel.objects.filter(email=user.email).first()
                    if staff and staff.role == RoleChoices.STAFF:
                        return redirect("sale")
                except StaffModel.DoesNotExist:
                    pass
    else:
        form = AccountAuthenticationForm()
    context["login_form"] = form

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'account.html', context)
