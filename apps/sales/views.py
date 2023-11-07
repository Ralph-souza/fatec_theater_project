from django.shortcuts import render, redirect

from apps.sales.forms import SalesForm


def sales_view(request):
    context = {}

    if request.POST:
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()

            return redirect('ticket.hmtl')
        
    else:
        sales_form = SalesForm()
    
    context["sales_form"] = sales_form
    return render(request, 'sales.html', context)
