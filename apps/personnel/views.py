from django.shortcuts import get_object_or_404, render, redirect

from apps.account.models import Account
from apps.personnel.forms import ManagerForm, StaffForm


def profile_view(request):
    context = {}
    email = request.session.get("email", None)

    if request.POST:
        role = request.POST.get("role")

        if role == "manager":
            form = ManagerForm(request.POST, initial={"email": email})
            is_admin = True
        elif role == "staff":
            form = StaffForm(request.POST, initial={"email": email})
            is_admin = False
        else:
            form = None
            is_admin = False

        if form is not None and form.is_valid():
            if role == "manager" or role == "staff":
                profile = form.save(commit=False)

                user = get_object_or_404(Account, email=form.cleaned_data["email"])
                profile.email = user
                profile.is_admin = is_admin
                profile.save()
            return redirect("login")

        context["profile_form"] = form
    else:
        context["manager_form"] = ManagerForm(initial={"email": email})
        context["staff_form"] = StaffForm(initial={"email": email})

    return render(request, "profile.html", context)
