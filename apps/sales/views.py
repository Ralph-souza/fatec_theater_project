from django.shortcuts import get_object_or_404, render, redirect

from apps.movies.models import RoomsModel

from apps.sales.models import SeatSelectionModel
from apps.sales.forms import SalesForm
# from apps.sales.utils import generate_seat_grid


def sales_view(request):
    context = {}

    if request.POST:
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()
            return redirect("seat")
        
    else:
        sales_form = SalesForm()

    context["sales_form"] = sales_form
    return render(request, "sales.html", context)


def seat_view(request, room_id):
    context = {}

    room = get_object_or_404(RoomsModel, pk=room_id)
    sold_seats = SeatSelectionModel.objects.filter(seat__room=room).values_list("seat__seat", flat=True)
    seat_number = room.seat
    # seat_grid = generate_seat_grid(seat_number, sold_seats)

    context = {
        "room": room,
        "seat_grid": seat_grid
    }

    return render(request, "seat.html", context)
