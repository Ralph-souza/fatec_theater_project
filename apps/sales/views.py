from django.shortcuts import  render, redirect

from apps.sales.models import SalesModel
from apps.sales.choices import RoomSeatsChoices
from apps.sales.forms import SalesForm



def sales_view(request):
    context = {}

    if 'available_seats' not in request.session:
        request.session['available_seats'] = [seat[0] for seat in RoomSeatsChoices.choices]

    available_seats = request.session['available_seats']

    if request.POST:
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            seat = sales_form.cleaned_data["seat"]
            if seat in available_seats:
                index = available_seats.index(seat)
                available_seats.pop(index)
            sales_form.save()
            return redirect("ticket")
    
    else:
        sales_form = SalesForm()

    context["sales_form"] = sales_form
    context["available_seats"] = available_seats
    return render(request, "sales.html", context)


def ticket_view(request):
    ticket = SalesModel.objects.latest("created_at")
    context = {"ticket": ticket}
    return render(request, "ticket.html", context)
