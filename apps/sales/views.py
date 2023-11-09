from django.shortcuts import render, redirect

from apps.sales.forms import SalesForm


def sales_view(request):
    context = {}

    if request.POST:
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()

            return redirect('ticket')
        
    else:
        sales_form = SalesForm()
    
    context["sales_form"] = sales_form

    if request.method == "GET" and "room" in request.GET:
        room_id = request.GET.get("room")
        sales_form.update_movie_choices(room_id)

    return render(request, 'sales.html', context)
